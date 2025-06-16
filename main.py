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

# Helper to run subprocess and handle errors
pipeline_status = []
def run_step(cmd, step_name):
    print(f"\n=== {step_name} ===")
    result = subprocess.run(cmd, capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print(f"[stderr] {result.stderr}")
    if result.returncode != 0:
        print(f"\n[ERROR] Step '{step_name}' failed with exit code {result.returncode}.")
        pipeline_status.append((step_name, False, result.stdout, result.stderr))
        print("Pipeline stopped due to error.")
        sys.exit(result.returncode)
    else:
        pipeline_status.append((step_name, True, result.stdout, result.stderr))

# Step 2: Data retrieval (downloads PDFs to ./pdfs)
data_retrieval_cmd = [
    sys.executable, 'data_retrieval.py'
] + [str(imo) for imo in args.imo_numbers]
run_step(data_retrieval_cmd, "Step 1: Retrieving data and saving PDFs")

# Step 3: Convert PDFs to images
pdf_to_img_cmd = [
    sys.executable, 'pdf_to_img.py'
]
run_step(pdf_to_img_cmd, "Step 2: Converting PDFs to images")

# Step 4: Extract data and jsonify
extraction_cmd = [
    sys.executable, 'extraction_and_jsonification.py'
]
run_step(extraction_cmd, "Step 3: Extracting data and saving JSONs")

# Step 5: Map and push final outputs to MongoDB
final_output_cmd = [
    sys.executable, 'final_output_and_push.py'
]
run_step(final_output_cmd, "Step 4: Mapping and pushing final outputs to MongoDB")

# print("\n--- Pipeline Summary ---")
# for step, success, out, err in pipeline_status:
#     status = "SUCCESS" if success else "FAILED"
#     print(f"{step}: {status}")
#     if not success:
#         print(f"  Output: {out}")
#         print(f"  Error: {err}")

if all(success for _, success, _, _ in pipeline_status):
    print("\nPipeline complete! All data extracted, mapped, and pushed to MongoDB.")
else:
    print("\nPipeline finished with errors. See above for details.") 