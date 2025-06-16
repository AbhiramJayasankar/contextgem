import os
import json
from contextgem import Document, DocumentLLM, Image, image_to_base64
from dotenv import load_dotenv
load_dotenv()

def process_image_and_extract_data(image_path, lab_name):
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
    elif lab_name == "vps_2":
        from jsonobjectconept_schemas.vps_2 import report_header_concept, oil_analysis_results_concept
    elif lab_name == "nof":
        from jsonobjectconept_schemas.nof import report_header_concept, oil_analysis_results_concept
    elif lab_name == "mobil":
        from jsonobjectconept_schemas.mobil import report_header_concept, oil_analysis_results_concept
    elif lab_name == "maritec":
        from jsonobjectconept_schemas.maritec import report_header_concept, oil_analysis_results_concept
    elif lab_name == "marlab":
        from jsonobjectconept_schemas.marlab import report_header_concept, oil_analysis_results_concept
    elif lab_name == "shell":
        from jsonobjectconept_schemas.shell import report_header_concept, oil_analysis_results_concept
    else:
        raise ValueError("Invalid lab_name specified. Please choose from castrol, chevron, enos, gulf, total, tribocare, viswa, vps, nof, mobil, maritec, marlab, or shell.")

    doc_image = Image(mime_type="image/jpeg", base64_data=image_to_base64(image_path))
    doc = Document(images=[doc_image])

    doc.add_concepts([report_header_concept, oil_analysis_results_concept])

    vlm = DocumentLLM(
        model="gemini/gemini-2.0-flash",
        api_key=os.getenv("GOOGLE_API_KEY"),
        role="extractor_vision",
    )

    extracted_concepts = vlm.extract_concepts_from_document(doc)

    report_header_data = extracted_concepts[0].extracted_items[0].value
    oil_analysis_data = extracted_concepts[1].extracted_items[0].value

    combined_output = {
        "report_header": report_header_data,
        "oil_analysis_results": oil_analysis_data
    }

    return combined_output




