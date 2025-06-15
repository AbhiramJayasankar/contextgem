import argparse
import subprocess
import sys
import os
import shutil

# Step 0: Clean up folders before starting
FOLDERS_TO_CLEAN = ["pdfs", "images", "extracted_jsons", "final_output"]
for folder in FOLDERS_TO_CLEAN:
    if os.path.exists(folder):
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

# Step 1: Parse IMO list from user input
parser = argparse.ArgumentParser(description="Full pipeline: Retrieve, convert, extract, jsonify, and push lab reports.")
parser.add_argument('imo_numbers', metavar='IMO', type=int, nargs='+', help='IMO numbers to process')
args = parser.parse_args()

# Step 2: Data retrieval (downloads PDFs to ./pdfs)
data_retrieval_cmd = [
    sys.executable, 'data_retrieval.py'
] + [str(imo) for imo in args.imo_numbers]
print("\n=== Step 1: Retrieving data and saving PDFs ===")
subprocess.run(data_retrieval_cmd, check=True)

# Step 3: Convert PDFs to images
pdf_to_img_cmd = [
    sys.executable, 'pdf_to_img.py'
]
print("\n=== Step 2: Converting PDFs to images ===")
subprocess.run(pdf_to_img_cmd, check=True)

# Step 4: Extract data and jsonify
extraction_cmd = [
    sys.executable, 'extraction_and_jsonification.py'
]
print("\n=== Step 3: Extracting data and saving JSONs ===")
subprocess.run(extraction_cmd, check=True)

# Step 5: Map and push final outputs to MongoDB
final_output_cmd = [
    sys.executable, 'final_output_and_push.py'
]
print("\n=== Step 4: Mapping and pushing final outputs to MongoDB ===")
subprocess.run(final_output_cmd, check=True)

print("\nPipeline complete! All data extracted, mapped, and pushed to MongoDB.") 