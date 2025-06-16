from contextgem import JsonObjectConcept
from typing import Union, List

report_header_concept = JsonObjectConcept(
    name="Marlab_Report_Header",
    llm_role="extractor_vision",
    description="""Extracts key customer and equipment information from the top section of the MARLAB oil analysis report.
    Information is spread across the top of the document.
    Identify empty sections and leave them blank.""",
    structure={
        "report_provider_company": Union[int, float, str, None],
        "report_id": Union[int, float, str, None],
        "equipment_information": {
            "company_name": Union[int, float, str, None],
            "vessel_name": Union[int, float, str, None],
            "imo_number": Union[int, float, str, None],
            "product_name": Union[int, float, str, None],
            "equipment_make": Union[int, float, str, None],
            "equipment_model": Union[int, float, str, None],
            "machinery_unit": Union[int, float, str, None],
            "sample_location": Union[int, float, str, None],
        }
    },
)

oil_analysis_results_concept = JsonObjectConcept(
    name="Marlab_Analysis_Results",
    llm_role="extractor_vision",
    description="""Each numbered column in the main results table is a separate sample; extract the data for each.
    The diagnosis remark at the bottom should be extracted into the diagnosis_remarks object.
    Leave empty cells as null.""",
    add_justifications=False,
    add_references=False,
    singular_occurrence=False,
    justification_depth="brief",
    justification_max_sents=2,
    structure={
        "samples": [
            {
                "sample_information": {
                    "lab_order_number": Union[int, float, str, None],
                    "date_received": Union[int, float, str, None],
                    "date_tested": Union[int, float, str, None],
                    "date_reported": Union[int, float, str, None],
                    "sampling_date": Union[int, float, str, None],
                },
                "usage_information": {
                    "lubricant_used": Union[int, float, str, None],
                    "fuel_used": Union[int, float, str, None],
                    "equipment_life_hours": Union[int, float, str, None],
                    "oil_life_hours": Union[int, float, str, None],
                    "oil_added_l": Union[int, float, str, None],
                    "lubricant_condition": Union[int, float, str, None],
                },
                "physical_properties": {
                    "viscosity_40c_mm2_s": Union[int, float, str, None],
                    "total_acid_number_mg_koh_g": Union[int, float, str, None],
                    "pq_index_wpi": Union[int, float, str, None],
                    "water_content_ppm": Union[int, float, str, None],
                },
                "element_analysis_ppm": {
                    "iron_ppm": Union[int, float, str, None],
                    "lead_ppm": Union[int, float, str, None],
                    "copper_ppm": Union[int, float, str, None],
                    "chromium_ppm": Union[int, float, str, None],
                    "aluminium_ppm": Union[int, float, str, None],
                    "nickel_ppm": Union[int, float, str, None],
                    "silver_ppm": Union[int, float, str, None],
                    "tin_ppm": Union[int, float, str, None],
                    "silicon_ppm": Union[int, float, str, None],
                    "boron_ppm": Union[int, float, str, None],
                    "sodium_ppm": Union[int, float, str, None],
                    "phosphorus_ppm": Union[int, float, str, None],
                    "zinc_ppm": Union[int, float, str, None],
                    "calcium_ppm": Union[int, float, str, None],
                    "barium_ppm": Union[int, float, str, None],
                    "magnesium_ppm": Union[int, float, str, None],
                    "vanadium_ppm": Union[int, float, str, None],
                    "molybdenum_ppm": Union[int, float, str, None],
                },
            }
        ],
        "diagnosis_remarks": {
            "remarks": Union[int, float, str, None],
        }
    },
)