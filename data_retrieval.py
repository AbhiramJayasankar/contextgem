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

# === CONFIGURATION ===
load_dotenv()

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# openai.api_key = OPENAI_API_KEY

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

# def llm_classify_lab_name(header_text: str, valid_labs: list) -> str:
#     prompt = (
#         f"Given the following PDF header text, classify which lab it is from this list: {', '.join(valid_labs)}.\n"
#         f"If none match, return 'UNKNOWN_LAB'.\n\n"
#         f"Header text:\n{header_text}\n"
#         f"Lab name:"
#     )
#     try:
#         client = openai.OpenAI(api_key=OPENAI_API_KEY)
#         response = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[{"role": "user", "content": prompt}],
#             max_tokens=10,
#             temperature=0
#         )
#         lab_name = response.choices[0].message.content.strip()
#         if lab_name in valid_labs:
#             return lab_name
#         else:
#             return "UNKNOWN_LAB"
#     except Exception as e:
#         print(f"LLM error: {e}")
#         return "ERROR_PARSING"

def find_first_lab_in_text(text: str) -> str:
    text_upper = text.upper()
    # Check original labs
    for lab in VALID_TESTLABS:
        if lab.upper() in text_upper:
            return lab
    # Check aliases
    for alias, actual in LAB_ALIASES.items():
        if alias.upper() in text_upper:
            return actual
    return "UNKNOWN_LAB"


def extract_lab_name_from_pdf(file_path: str) -> str:
    try:
        doc = fitz.open(file_path)
        page = doc[0]

        # # Extract text blocks
        # blocks = page.get_text("blocks")
        # block_text = " ".join(
        #     block[4].strip().upper()
        #     for block in blocks
        #     if block[1] < 250 and block[4].strip()
        # )

        # OCR on header
        page_width = page.rect.width
        header_clip = fitz.Rect(0, 0, page_width, 250)
        pix = page.get_pixmap(clip=header_clip, dpi=300)
        img_bytes = pix.tobytes("png")
        image = Image.open(io.BytesIO(img_bytes))
        ocr_text = pytesseract.image_to_string(image).upper()

        # Combine all header text
        # joined_text = block_text + "\n" + ocr_text
        joined_text = ocr_text
        # print(f"Joined text: {joined_text}")

        lab_from_llm = find_first_lab_in_text(joined_text)
        if lab_from_llm:
            return lab_from_llm
        return "UNKNOWN_LAB"
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
        # found = list(collection.find({"imo": imo}))
        found = collection.find_one({"imo": imo, "testLab": "Chevron"})
        if not found:
            print(f"No documents found for IMO: {imo}")
        else:
            print(f"Found {len(found)} documents for IMO {imo}")
            # docs.extend(found)
            docs.append(found)

    if not docs:
        print(f"No documents found for any IMO in list: {IMO_NUMBERS}")
        sys.exit(0)

    print(f"Total documents found: {len(docs)}")

    # === PROCESSING LOOP ===
    for doc in docs:
        for url in doc.get("location", []):
            if isinstance(url, str) and url.startswith("http"):
                download_and_sort_pdf(url)
            else:
                print(f"Invalid or empty URL skipped in doc {doc.get('_id')}")
