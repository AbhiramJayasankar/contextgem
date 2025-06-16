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
import cv2
from contextgem import Document, DocumentLLM, StringConcept, image_to_base64, Image
import json

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
    "lubmarine": "Total",
    "Mobil Serv": "MobilServ"
}
TIMEOUT = 10
BASE_DOWNLOAD_DIR = "./pdfs"

ALL_LABS = VALID_TESTLABS + list(LAB_ALIASES.keys())
    
def get_canonical_lab_name(lab_name: str) -> str:
    """Convert lab name to its canonical form using aliases."""
    if not lab_name:
        return "ERROR_PARSING"
        
    # Convert to lowercase for case-insensitive comparison
    lab_name_lower = lab_name.lower()
    
    # Check if it's an alias (case-insensitive)
    for alias, canonical in LAB_ALIASES.items():
        if lab_name_lower == alias.lower():
            print(f"Converting alias '{lab_name}' to canonical name '{canonical}'")
            return canonical
    
    # If not an alias, check if it's a valid lab name (case-insensitive)
    for valid_lab in VALID_TESTLABS:
        if lab_name_lower == valid_lab.lower():
            return valid_lab
            
    print(f"Warning: Unknown lab name '{lab_name}' - using as is")
    return lab_name

def extract_lab_report_provider_from_pdf(file_path):
    """
    Extracts the lab report provider from the top quarter of a PDF's first page.
    Uses OpenCV for image processing and contextgem for lab name extraction.
    """
    try:
        # Open PDF and get first page as image
        doc = fitz.open(file_path)
        page = doc[0]
        
        # Convert page to image
        pix = page.get_pixmap()
        img_bytes = pix.tobytes("png")
        doc.close()
        
        # Save to temp file for OpenCV
        import tempfile
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
            tmp.write(img_bytes)
            tmp_path = tmp.name
        
        # Process with OpenCV
        img = cv2.imread(tmp_path)
        if img is None:
            raise FileNotFoundError(f"Could not read the image file: {tmp_path}")

        # Crop to top quarter
        height, width, _ = img.shape
        top_quarter_height = height // 4
        cropped_img = img[0:top_quarter_height, 0:width]
        
        # Convert to base64
        _, buffer = cv2.imencode('.jpg', cropped_img)
        cropped_base64 = base64.b64encode(buffer).decode('utf-8')
        
        # Clean up temp file
        os.unlink(tmp_path)
        
        # Use contextgem for extraction
        doc_image = Image(mime_type="image/jpeg", base64_data=cropped_base64)
        doc = Document(images=[doc_image])
        
        name_concept = StringConcept(
            name="lab_report_provider_company",
            llm_role="extractor_vision",
            description="""Name of the company that provided the report,
            extracted from the company logo in the top section of the image
            it should be one of these 10,
            castrol,chevron,eneos,gulf,lubmarine,mobil,tribocare,viswa,vps,nof""",
        )
        
        doc.add_concepts([name_concept])
        
        vlm = DocumentLLM(
            model="gemini/gemini-2.0-flash",
            api_key=os.getenv("GOOGLE_API_KEY"),
            role="extractor_vision",
        )
        
        extracted_concepts = vlm.extract_concepts_from_document(doc)
        
        # Check if any items were extracted before accessing the value
        if extracted_concepts and extracted_concepts[0].extracted_items:
            return extracted_concepts[0].extracted_items[0].value
        else:
            return "Provider not found"
            
    except Exception as e:
        print(f" Error processing PDF {file_path}: {e}")
        return "ERROR_PARSING"

# Replace extract_lab_name_from_pdf with the new provider
extract_lab_name_from_pdf = extract_lab_report_provider_from_pdf

def extract_lab_from_s3_url(url: str):
    """
    Extracts the lab name from an S3 URL by parsing the segment after 'split/'.
    """
    try:
        parts = url.split("split/")
        if len(parts) > 1:
            return parts[1].split("/")[0]  # Extract the lab name
        return "Unknown"
    except Exception as e:
        print(f"Error extracting lab from S3 URL: {e}")
        return "Unknown"


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

            # Classify and get canonical lab name
            if "shipsight.synergymarinegroup.com" in url or "Fast%20Report" in url:
                print("USING CONTEXTGEN FOR LABNAME")
                raw_lab_name = extract_lab_name_from_pdf(temp_path)
                print(f"Raw lab name detected: '{raw_lab_name}'")
                lab_name = get_canonical_lab_name(raw_lab_name)
            else:
                print("EXTRACTING LABNAME FORM S3 LINK")
                raw_lab_name_ = extract_lab_from_s3_url(url)
                lab_name_ = get_canonical_lab_name(raw_lab_name_)
                print(f"Lab name extracted from S3 URL: '{lab_name_}'")

            final_dir = os.path.join(BASE_DOWNLOAD_DIR, lab_name)
            Path(final_dir).mkdir(parents=True, exist_ok=True)

            final_path = os.path.join(final_dir, file_name)
            os.rename(temp_path, final_path)
            print(f"Moved to {final_path} (Lab: {lab_name})")

            # Save mapping from relative PDF path to URL
            rel_pdf_path = os.path.relpath(final_path, BASE_DOWNLOAD_DIR)
            pdf_link_map[rel_pdf_path] = url
        else:
            print(f"Skipped non-PDF or failed request ({r.status_code}) for {url}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

def normalize_url(url: str) -> str:
    """
    Replaces all backslashes in the URL with forward slashes.
    """
    return url.replace('\\', '/')

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
        # found = collection.find_one({"imo": imo, "testLab": "Total"})
        if not found:
            print(f"No documents found for IMO: {imo}")
        else:
            print(f"Found {len(found)} documents for IMO {imo}")
            docs.extend(found)
            # docs.append(found

    if not docs:
        print(f"No documents found for any IMO in list: {IMO_NUMBERS}")
        sys.exit(1)

    print(f"Total documents found: {len(docs)}")

    # === PROCESSING LOOP ===
    pdf_link_map = {}
    for doc in docs:
        for url in doc.get("location", []):
            if isinstance(url, str) and url.startswith("http"):
                normalized_url = normalize_url(url)
                download_and_sort_pdf(normalized_url)
            else:
                print(f"Invalid or empty URL skipped in doc {doc.get('_id')}")

    if pdf_link_map:
        PDF_LINK_MAP_PATH = os.path.join(BASE_DOWNLOAD_DIR, "pdf_link_map.json")
        with open(PDF_LINK_MAP_PATH, "w") as f:
            json.dump(pdf_link_map, f, indent=2)
        print(f"PDF link map saved to {PDF_LINK_MAP_PATH}")
    else:
        print("No PDFs downloaded, so no link map saved.")




