from contextgem import JsonObjectConcept
from typing import Union, List

# Updated report_header_concept with the new standardized structure
report_header_concept = JsonObjectConcept(
    name="Lubmarine_Report_Header",
    llm_role="extractor_vision",
    description="Extracts key header information from the Lubmarine report using a standardized structure.",
    structure={
        "report_provider_company": Union[int, float, str, None],
        "overall_lubricant_condition": Union[int, float, str, None],
        "equipment_information": {
            "customer_name": Union[int, float, str, None],
            "vessel_name": Union[int, float, str, None],
            "imo_number": Union[int, float, str, None],
            "report_date": Union[int, float, str, None],
            "product_name": Union[int, float, str, None],
            "equipment_make": Union[int, float, str, None],
            "equipment_model": Union[int, float, str, None],
            "machinery_unit": Union[int, float, str, None],
            "equipment_sn": Union[int, float, str, None],
            "sample_location": Union[int, float, str, None],
        }
    },
)

# The existing oil_analysis_results_concept remains the same
oil_analysis_results_concept = JsonObjectConcept(
    name="Lubmarine_Analysis_Results",
    llm_role="extractor_vision",
    description="""Each column in the DATA table is a separate sample; extract the data for each.
    The Symptoms and Comments should be extracted into the summary object.
    Leave empty cells as null.""",
    add_justifications=False,
    add_references=False,
    singular_occurrence=False,
    justification_depth="brief",
    justification_max_sents=2,
    structure={
        "summary": {
            "symptoms": Union[int, float, str, None],
            "comments": Union[int, float, str, None],
        },
        "samples": [
            {
                "sample_details": {
                    "status": Union[int, float, str, None],
                    "sample_no": Union[int, float, str, None],
                    "date_received": Union[int, float, str, None],
                    "date_reported": Union[int, float, str, None],
                    "oil_on_label": Union[int, float, str, None],
                    "purifier_filter": Union[int, float, str, None],
                    "equipment_life": Union[int, float, str, None],
                    "oil_life": Union[int, float, str, None],
                    "top_up_volume": Union[int, float, str, None],
                },
                "analysis": {
                    "visco_40c_mm2s": Union[int, float, str, None],
                    "visco_100c_mm2s": Union[int, float, str, None],
                    "water_content_percent_mass": Union[int, float, str, None],
                    "tbn_mgkoh_g": Union[int, float, str, None],
                    "pq_index": Union[int, float, str, None],
                    "oxidation_by_ftir_abs_cm": Union[int, float, str, None],
                },
                "spectro_analysis": {
                    "wear_elements": {
                        "iron_fe": Union[int, float, str, None],
                        "chromium_cr": Union[int, float, str, None],
                        "molybdenum_mo": Union[int, float, str, None],
                        "copper_cu": Union[int, float, str, None],
                        "lead_pb": Union[int, float, str, None],
                        "silver_ag": Union[int, float, str, None],
                        "tin_sn": Union[int, float, str, None],
                        "aluminum_al": Union[int, float, str, None],
                    },
                    "contaminants": {
                        "nickel_ni": Union[int, float, str, None],
                        "vanadium_v": Union[int, float, str, None],
                        "silicon_si": Union[int, float, str, None],
                        "sodium_na": Union[int, float, str, None],
                        "boron_b": Union[int, float, str, None],
                        "potassium_k": Union[int, float, str, None],
                        "magnesium_mg": Union[int, float, str, None],
                    },
                    "other_metals": {
                        "phosphorus_p": Union[int, float, str, None],
                        "zinc_zn": Union[int, float, str, None],
                        "barium_ba": Union[int, float, str, None],
                        "calcium_ca": Union[int, float, str, None],
                    },
                },
            }
        ],
    },
)