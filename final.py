import os
import json
from extract_functions.extract import process_image_and_extract_data
from extract_functions.json_merge import merge_all_jsons
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define root folders for input and output
root_input_directory = "images"
root_output_directory = "extracted_jsons"

print("--- Starting Folder-Based Extraction and Saving Process ---")

# Walk through the input directory structure
for dirpath, dirnames, filenames in os.walk(root_input_directory):
    
    image_files = [f for f in filenames if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    if not image_files:
        continue

    print(f"\nProcessing Report Folder: {dirpath}")
    print("-" * 50)
    
    jsons_in_this_report = []
    for filename in image_files:
        image_path = os.path.join(dirpath, filename)
        path_parts = os.path.normpath(dirpath).split(os.sep)

        if len(path_parts) > 1:
            lab_name = path_parts[1]
            final_lab_name = lab_name
            if lab_name == "vps":
                if "page_1" in filename.lower():
                    final_lab_name = "vps"
                elif "page_2" in filename.lower():
                    final_lab_name = "vps_2"

            print(f"  - Extracting from: {filename}...")
            
            try:
                extracted_data = process_image_and_extract_data(image_path, final_lab_name)
                jsons_in_this_report.append(extracted_data)
                print("    Status: Success")

            except IndexError:
                print("    Status: Failed - nothing to extract in the specified page")
            except Exception as e:
                print(f"   Status: Failed - An unexpected error occurred: {e}")

    # --- START: New Saving Logic ---
    final_output = None
    if len(jsons_in_this_report) > 1:
        print(f"\nMerging {len(jsons_in_this_report)} pages for report...")
        final_output = merge_all_jsons(jsons_in_this_report)
    elif len(jsons_in_this_report) == 1:
        print("\nSingle page report, no merge needed.")
        final_output = jsons_in_this_report[0]

    # If there is a JSON object to save (either merged or single)
    if final_output:
        try:
            # 1. Determine the output path and filename
            # This gets the path relative to the 'images' folder, e.g., 'castrol\Castrol LO report'
            relative_path = os.path.relpath(dirpath, root_input_directory)
            # The lab folder part, e.g., 'castrol'
            output_subfolder = os.path.dirname(relative_path)
            # The report folder name, e.g., 'Castrol LO report'
            json_filename = f"{os.path.basename(relative_path)}.json"

            # Create the full path for the output folder, e.g., 'extracted_jsons\castrol'
            output_dir = os.path.join(root_output_directory, output_subfolder)
            
            # 2. Create the directory structure if it doesn't exist
            os.makedirs(output_dir, exist_ok=True)
            
            # Create the full path for the output file
            output_filepath = os.path.join(output_dir, json_filename)

            # 3. Write the JSON data to the file
            with open(output_filepath, 'w') as f:
                json.dump(final_output, f, indent=4)
            
            print(f"Successfully saved report to: {output_filepath}")

        except Exception as e:
            print(f"Error saving file for report {dirpath}. Reason: {e}")
    else:
        print(f"\nNo data was successfully extracted from {dirpath} to save.")
    
    print("-" * 50)
    # --- END: New Saving Logic ---

print("\n\n--- Process Complete ---")