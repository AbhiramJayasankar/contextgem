import os 
import json
from pymongo import MongoClient
from fieldmappings import *
import re
from dotenv import load_dotenv

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
    "mobilserv": mobilserv_field_map,
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
            # Check if part includes a list index like samples[0]
            match = re.match(r"(\w+)\[(\d+)\]", part)
            if match:
                key, index = match.group(1), int(match.group(2))
                current = current.get(key, [])
                if isinstance(current, list) and 0 <= index < len(current):
                    current = current[index]
                else:
                    return ""
            else:
                current = current.get(part, "")
        else:
            return ""
    return current if current is not None else ""

def get_samples_mapping(data: dict, sample_format_dict: dict) -> str:
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
        all_sample_details.append(one_sample)
    return all_sample_details

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
        else:
            # Only call get_samples_mapping if it's a list and first element is a dict
            if isinstance(field_map_dict[key], list) and len(field_map_dict[key]) > 0 and isinstance(field_map_dict[key][0], dict):
                result_map[key] = get_samples_mapping(json_data, field_map_dict[key][0])
            else:
                result_map[key] = field_map_dict[key]
    return result_map

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

# Walk through all JSON files in extracted_jsons
for root, dirs, files in os.walk(EXTRACTED_JSONS_DIR):
    for file in files:
        if file.endswith(".json"):
            json_path = os.path.join(root, file)
            with open(json_path, "r") as f:
                data = json.load(f)
            lab_name = get_lab_name_from_path(json_path)
            mapped = map_fields(lab_name, data)
            if mapped:
                # Save to final_output/lab_name/filename
                lab_output_dir = os.path.join(FINAL_OUTPUT_DIR, lab_name)
                os.makedirs(lab_output_dir, exist_ok=True)
                output_path = os.path.join(lab_output_dir, file)
                with open(output_path, "w") as out_f:
                    json.dump(mapped, out_f, indent=2)
                print(f"Dumped mapped output for {file} (lab: {lab_name}) to {output_path}.")
                collection.insert_one(mapped)
                print(f"Pushed mapped output for {file} (lab: {lab_name}) to MongoDB.")
            else:
                print(f"Skipped {file} (no mapping for lab: {lab_name})") 