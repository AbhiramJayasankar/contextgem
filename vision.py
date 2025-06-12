import os
import json
from contextgem import Aspect, Document, DocumentLLM, StringConcept, DocxConverter, JsonObjectConcept
from contextgem import Document, DocumentLLM, Image, NumericalConcept, image_to_base64
from typing import Union
from dotenv import load_dotenv
from jsonobjectconept_schemas.castrol import report_header_concept, oil_analysis_results_concept

load_dotenv()

doc_image = Image(mime_type="image/jpeg", base64_data=image_to_base64("images\\castrol_sample-images-0.jpg"))
doc = Document(
    images=[doc_image],  
)

# Attach the concept to the document
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

# Access the extracted dictionary from the concept
extracted_data = extracted_concepts[0].extracted_items[0].value
pretty_json_output = json.dumps(extracted_data, indent=4)

print("--- Extracted Oil Analysis Report Header ---")
print(pretty_json_output)

extracted_data = extracted_concepts[1].extracted_items[0].value
pretty_json_output = json.dumps(extracted_data, indent=4)

print("--- Extracted Oil Analysis Details ---")
print(pretty_json_output)