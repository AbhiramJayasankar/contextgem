import os
import requests
import fitz  # PyMuPDF
from pymongo import MongoClient
from urllib.parse import urlparse
from pathlib import Path
import pytesseract
from PIL import Image
import io
import argparse
import sys
from dotenv import load_dotenv
import openai
import difflib
import base64

# === CONFIGURATION ===
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = "syia-etl-dev"
COLLECTION_NAME = "lube_oil_common_collection"

# IMO_NUMBERS will be set from command line
VALID_TESTLABS = [
    "Castrol", "Chevron", "ENEOS", "Gulf", "Total",
    "Tribocare", "Viswa", "VPS", "NOF", "MobilServ"
]
LAB_ALIASES = {
    "LUBDIAG": "Total",
    "Mobil Serv": "MobilServ"
}
TIMEOUT = 10
BASE_DOWNLOAD_DIR = "./pdfs"

ALL_LABS = VALID_TESTLABS + list(LAB_ALIASES.keys())

def llm_classify_lab_name(image, valid_labs: list, lab_aliases: dict) -> str:
    """
    Sends the image to OpenAI's gpt-4o-mini model to classify the lab name.
    Includes information about lab aliases in the prompt.
    """
    # Create alias information string
    alias_info = "Lab aliases: " + ", ".join([f"{alias} -> {actual}" for alias, actual in lab_aliases.items()])
    
    prompt = (
        f"You are given the top portion of a PDF first page containing a lab test report. "
        f"Classify the lab from this list: {', '.join(ALL_LABS)}. "
        f"Lab aliases: {alias_info}. "
        f"ONLY use the logo or company name appearing in the top header of the page. "
        f"If you see a lab alias, return the canonical lab name. "
        f"If no known lab name or alias is visible in the top branding section, return 'UNKNOWN_LAB'."
    )
    try:
        # Convert image to base64
        buffered = io.BytesIO()
        image.save(buffered, format="PNG")
        img_b64 = base64.b64encode(buffered.getvalue()).decode()
        client = openai.OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img_b64}"}}
                ]}
            ],
            max_tokens=10,
            temperature=0
        )
        lab_name = response.choices[0].message.content.strip()
        # Map alias to canonical
        if lab_name in lab_aliases:
            # print(f"Lab found in aliases: {lab_name}")
            return lab_aliases[lab_name]
        if lab_name in valid_labs:
            # print(f"Lab found in valid labs: {lab_name}")
            return lab_name
        return "UNKNOWN_LAB"
    except Exception as e:
        print(f"LLM error: {e}")
        return "ERROR_PARSING"
    
def extract_lab_name_from_pdf(file_path: str) -> str:
    try:
        doc = fitz.open(file_path)
        page = doc[0]
        # Extract header region as image (top 200px)
        header_clip = fitz.Rect(0, 0, page.rect.width, 200)
        pix = page.get_pixmap(clip=header_clip)
        img_bytes = pix.tobytes("png")
        image = Image.open(io.BytesIO(img_bytes))
        # OCR
        ocr_text = pytesseract.image_to_string(image).upper()
        # print(ocr_text)
        for lab in ALL_LABS:
            if lab.upper() in ocr_text:
                doc.close()
                # print(f"Lab found in OCR: {lab}")
                return LAB_ALIASES.get(lab, lab)
        # Fallback: send full page to LLM
        page_image = Image.open(io.BytesIO(page.get_pixmap().tobytes("png")))
        lab_name = llm_classify_lab_name(page_image, VALID_TESTLABS, LAB_ALIASES)
        doc.close()
        return lab_name
    except Exception as e:
        print(f"❗ Error processing PDF {file_path}: {e}")
        return "ERROR_PARSING"

def download_and_sort_pdf(url: str):
    try:
        file_name = os.path.basename(urlparse(url).path)
        temp_path = os.path.join(BASE_DOWNLOAD_DIR, "__temp__", file_name)
        Path(os.path.dirname(temp_path)).mkdir(parents=True, exist_ok=True)

        # Download
        print(f"Downloading {url}")
        r = requests.get(url, timeout=TIMEOUT)
        if r.status_code == 200 and "application/pdf" in r.headers.get("Content-Type", ""):
            with open(temp_path, "wb") as f:
                f.write(r.content)
            print(f"Downloaded to {temp_path}")

            # Classify
            lab_name = extract_lab_name_from_pdf(temp_path)
            final_dir = os.path.join(BASE_DOWNLOAD_DIR, lab_name)
            Path(final_dir).mkdir(parents=True, exist_ok=True)

            final_path = os.path.join(final_dir, file_name)
            os.rename(temp_path, final_path)
            print(f"📁 Moved to {final_path}")
        else:
            print(f"Skipped non-PDF or failed request ({r.status_code}) for {url}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download and sort PDFs for given IMO numbers.")
    parser.add_argument('imo_numbers', metavar='IMO', type=int, nargs='+', help='IMO numbers to process')
    args = parser.parse_args()
    IMO_NUMBERS = args.imo_numbers

    # === DB SETUP ===
    client = MongoClient(MONGO_URI)
    collection = client[DB_NAME][COLLECTION_NAME]

    docs = []
    for imo in IMO_NUMBERS:
        found = list(collection.find({"imo": imo}))
        # found = collection.find_one({"imo": imo, "testLab": "Castrol"})
        if not found:
            print(f"No documents found for IMO: {imo}")
        else:
            print(f"Found {len(found)} documents for IMO {imo}")
            docs.extend(found)
            # docs.append(found)

    if not docs:
        print(f"No documents found for any IMO in list: {IMO_NUMBERS}")
        sys.exit(1)

    print(f"Total documents found: {len(docs)}")

    # === PROCESSING LOOP ===
    for doc in docs:
        for url in doc.get("location", []):
            if isinstance(url, str) and url.startswith("http"):
                download_and_sort_pdf(url)
            else:
                print(f"Invalid or empty URL skipped in doc {doc.get('_id')}")
