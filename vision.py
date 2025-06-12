import os
import json
from contextgem import Document, DocumentLLM, Image, image_to_base64
from dotenv import load_dotenv
load_dotenv()

lab_name="" #castrol/chevron/enos/gulf/total/tribocare/viswa/vps

if lab_name == "castrol":
    from jsonobjectconept_schemas.castrol import report_header_concept, oil_analysis_results_concept
elif lab_name == "chevron":
    from jsonobjectconept_schemas.chevron import report_header_concept, oil_analysis_results_concept
elif lab_name == "enos":
    from jsonobjectconept_schemas.enos import report_header_concept, oil_analysis_results_concept
elif lab_name == "gulf":
    from jsonobjectconept_schemas.gulf import report_header_concept, oil_analysis_results_concept
elif lab_name == "total":
    from jsonobjectconept_schemas.total import report_header_concept, oil_analysis_results_concept
elif lab_name == "tribocare":
    from jsonobjectconept_schemas.tribocare import report_header_concept, oil_analysis_results_concept
elif lab_name == "viswa":
    from jsonobjectconept_schemas.viswa import report_header_concept, oil_analysis_results_concept
elif lab_name == "vps":
    from jsonobjectconept_schemas.vps import report_header_concept, oil_analysis_results_concept
else:
    raise ValueError("Invalid lab_name specified. Please choose from castrol, chevron, enos, gulf, total, tribocare, viswa, or vps.")








image_path = "images\\vps\\VPS LO report\\page_1.png"
doc_image = Image(mime_type="image/jpeg", base64_data=image_to_base64(image_path))
doc = Document(
    images=[doc_image],  
)

doc.add_concepts([report_header_concept,oil_analysis_results_concept])



vlm_1 = DocumentLLM(
    model="openai/gpt-4o",
    api_key=os.getenv("OPENAI_API_KEY"),
    role="extractor_vision", 
)

vlm_2 = DocumentLLM(
    model="gemini/gemini-2.0-flash",
    # model="gemini/gemini-2.5-flash-preview-05-20",
    api_key=os.getenv("GOOGLE_API_KEY"),
    role="extractor_vision",
)

extracted_concepts = vlm_2.extract_concepts_from_document(doc)

report_header_data = extracted_concepts[0].extracted_items[0].value
oil_analysis_data = extracted_concepts[1].extracted_items[0].value

pretty_json_output = json.dumps(report_header_data, indent=4)

combined_output = {
    "report_header": report_header_data,
    "oil_analysis_results": oil_analysis_data
}

# Save extracted data to a JSON file in a structured directory
output_base_dir = "result_log"

relative_path = os.path.relpath(os.path.dirname(image_path), "images")
input_filename_without_ext = os.path.splitext(os.path.basename(image_path))[0]
json_filename = f"{input_filename_without_ext}.json"

output_dir_full_path = os.path.join(output_base_dir, relative_path)
os.makedirs(output_dir_full_path, exist_ok=True)
output_filepath = os.path.join(output_dir_full_path, json_filename)

with open(output_filepath, 'w') as json_file:
    json.dump(combined_output, json_file, indent=4)
print(json.dumps(combined_output, indent=4))
