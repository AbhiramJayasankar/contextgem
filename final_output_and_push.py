import os 
import json
from pymongo import MongoClient
from fieldmappings import *
import re
from dotenv import load_dotenv
import datetime
import copy

# MongoDB config (reuse from data_retrieval.py or set here)
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = "syia-etl-dev"
COLLECTION_NAME = "parsed_lube_oil_reports"

EXTRACTED_JSONS_DIR = "extracted_jsons"
FINAL_OUTPUT_DIR = "final_output"

# Map lab name to field mapping variable
LAB_FIELD_MAPS = {
    "castrol": castrol_field_map,
    "chevron": chevron_field_map,
    "eneos": eneos_field_map,
    "gulf": gulf_field_map,
    "total": total_field_map,
    "tribocare": tribocare_field_map,
    "viswa": viswa_field_map,
    "vps": vps_field_map,
    "nof": nof_field_map,
    "mobil": mobilserv_field_map,
    "shell": shell_field_map,
    "maritec": maritec_field_map,
    "marlab": marlab_field_map,
}

def get_lab_name_from_path(path):
    # Assumes path like extracted_jsons/LABNAME/...
    return os.path.basename(os.path.dirname(path)).lower()

def get_json_value(data: dict, field_path: str) -> str:
    """Retrieve a value from nested dict using dot-separated path, with list index support."""
    current = data
    parts = field_path.split(".")
    for part in parts:
        if isinstance(current, dict):
            # Support negative indices
            match = re.match(r"(\w+)\[(-?\d+)\]", part)
            if match:
                key, index = match.group(1), int(match.group(2))
                current = current.get(key, [])
                if isinstance(current, list) and -len(current) <= index < len(current):
                    current = current[index]
                else:
                    return ""
            else:
                current = current.get(part, "")
        else:
            return ""
    return current

def get_samples_mapping(data: dict, sample_format_dict: dict) -> list:
    num_samples = len(data["oil_analysis_results"]["samples"])
    all_sample_details = []
    for i in range(num_samples):
        one_sample = {}
        for key in sample_format_dict:
            if isinstance(sample_format_dict[key], dict):
                one_sample_details = {}
                for sub_key in sample_format_dict[key]:
                    path = sample_format_dict[key][sub_key]
                    if path is not None and 'samples[]' in path:
                        new_path = path.replace('samples[]', f'samples[{i}]')
                        one_sample_details[sub_key] = get_json_value(data, new_path)
                    elif path is not None:
                        one_sample_details[sub_key] = get_json_value(data, path)
                    else:
                        one_sample_details[sub_key] = None
                one_sample[key] = one_sample_details
            else:
                path = sample_format_dict[key]
                if path is not None and 'samples[]' in path:
                    new_path = path.replace('samples[]', f'samples[{i}]')
                    one_sample[key] = get_json_value(data, new_path)
                elif path is not None:
                    one_sample[key] = get_json_value(data, path)
                else:
                    one_sample[key] = None
        all_sample_details.append(one_sample)
    return all_sample_details

# def order_mother_fields(data):
#     """Manually order the top-level fields in a specific order."""
#     ordered_fields = [
#         "testLab",
#         "vesselName",
#         "imo",
#         "SampleIdentification",
#         "EquipmentInformation",
#         "Samples",
#         "AnalysisResults",
#         "QualityAndCompliance"
#     ]
    
#     # Create new dict with ordered fields
#     ordered_data = {}
#     for field in ordered_fields:
#         if field in data:
#             ordered_data[field] = data[field]
    
#     # Add any remaining fields that weren't in our order list
#     for field in data:
#         if field not in ordered_fields:
#             ordered_data[field] = data[field]
            
#     return ordered_data

def create_final_json(json_data, field_map_dict):
    result_map = {}
    for key in field_map_dict:
        if isinstance(field_map_dict[key], dict):
            result_map[key] = {}
            for sub_key in field_map_dict[key]:
                path = field_map_dict[key][sub_key]
                if path is not None:
                    result_map[key][sub_key] = get_json_value(json_data, path)
                else:
                    result_map[key][sub_key] = None
        elif isinstance(field_map_dict[key], str):
            if "." in field_map_dict[key]:
                result_map[key] = get_json_value(json_data, field_map_dict[key])
            else:
                result_map[key] = field_map_dict[key]
        elif isinstance(field_map_dict[key], list) and len(field_map_dict[key]) > 0 and isinstance(field_map_dict[key][0], dict):
            result_map[key] = get_samples_mapping(json_data, field_map_dict[key][0])
        else:
            result_map[key] = field_map_dict[key]
    return result_map
    # Order the mother fields
    # return order_mother_fields(result_map)

def map_fields(lab_name, data):
    field_map = LAB_FIELD_MAPS.get(lab_name)
    if not field_map:
        print(f"No field mapping for lab: {lab_name}")
        return None
    mapped_output = create_final_json(data, field_map)
    return mapped_output

# Connect to MongoDB
client = MongoClient(MONGO_URI)
collection = client[DB_NAME][COLLECTION_NAME]

PDF_LINK_MAP_PATH = os.path.join("pdfs", "pdf_link_map.json")
if os.path.exists(PDF_LINK_MAP_PATH):
    with open(PDF_LINK_MAP_PATH, "r") as f:
        pdf_link_map = json.load(f)
else:
    pdf_link_map = {}

# # Helper function to capitalize only the first letter if not already uppercase
# def smart_capitalize(lab_name):
#     if len(lab_name) == 0:
#         return lab_name
#     if lab_name.isupper():
#         return lab_name  # Already all caps, e.g., ENOS
#     return lab_name[0].upper() + lab_name[1:]

# Walk through all JSON files in extracted_jsons
for root, dirs, files in os.walk(EXTRACTED_JSONS_DIR):
    for file in files:
        if file.endswith(".json"):
            json_path = os.path.join(root, file)
            with open(json_path, "r") as f:
                data = json.load(f)
            lab_name = get_lab_name_from_path(json_path)
            report_folder = os.path.splitext(os.path.basename(json_path))[0]  # e.g., '11622704'
            print(f"Lab name: {lab_name}")
            rel_pdf_path = os.path.join(lab_name.lower(), f"{report_folder}.pdf")
            print(f"Rel PDF path: {rel_pdf_path}")
            pdf_info = pdf_link_map.get(rel_pdf_path, {})
            pdf_link = pdf_info.get("url")
            vessel_name_from_map = pdf_info.get("vesselName")
            imo_from_map = pdf_info.get("imo")
            mapped = map_fields(lab_name, data)
            if mapped:
                if imo_from_map is not None:
                    mapped["imo"] = imo_from_map
                if vessel_name_from_map is not None:
                    mapped["vesselName"] = vessel_name_from_map
                created_at = datetime.datetime.now(datetime.UTC)
                mapped["pdfLink"] = pdf_link
                mapped["createdAt"] = created_at

                # Save to final_output/lab_name/filename
                lab_output_dir = os.path.join(FINAL_OUTPUT_DIR, lab_name)
                os.makedirs(lab_output_dir, exist_ok=True)
                output_path = os.path.join(lab_output_dir, file)

                # Make a copy for local save, convert createdAt to string
                mapped_for_file = copy.deepcopy(mapped)
                mapped_for_file["createdAt"] = created_at.isoformat()

                with open(output_path, "w") as out_f:
                    json.dump(mapped_for_file, out_f, indent=2)
                print(f"Dumped mapped output for {file} (lab: {lab_name}) to {output_path}.")

                result = collection.insert_one(mapped)
                print(f"Pushed mapped output for {file} (lab: {lab_name}) to MongoDB. _id: {result.inserted_id}")
            else:
                print(f"Skipped {file} (no mapping for lab: {lab_name})") 