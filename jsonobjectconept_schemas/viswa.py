from contextgem import JsonObjectConcept
from typing import Union, List

report_header_concept = JsonObjectConcept(
    name="Viswa Lab Report Metadata",
    llm_role="extractor_vision",
    description="Extract key header, footer, and summary information from the Viswa Lab oil trend report.",
    structure={
        "report_provider_company": Union[int, float, str, None],
        "overall_oil_condition": Union[int, float, str, None],
        "customer_details": {
            "vessel": Union[str, None],
            "imo_no": Union[int, None],
            "customer": Union[int, float, str, None],
            "equipment": Union[int, float, str, None],
            "sampling_point": Union[int, float, str, None],
            "brand_and_grade": Union[int, float, str, None],


        },
        "po_number": Union[int, float, str, None],
        "comments": Union[int, float, str, None],
        "signed_by": Union[int, float, str, None],
        "lab_address": Union[int, float, str, None],
    },
) 

oil_analysis_results_concept = JsonObjectConcept(
    name="Viswa Lab Report Results",
    llm_role="extractor_vision",
    description="Extract the detailed test results for each sample column. Each column is a separate sample entry.",
    singular_occurrence=False,
    structure={
        "samples": [
            {
                "general_details": {
                    "report_id": Union[int, float, str, None],
                    "bottle_identification_no": Union[int, float, str, None],
                    "sampling_date": Union[int, float, str, None],
                    "sampling_point": Union[int, float, str, None],
                    "report_date": Union[int, float, str, None],
                    "place": Union[int, float, str, None],
                    "unit_usage": Union[int, float, str, None],
                    "total_lubricant_hours": Union[int, float, str, None],
                    "oil_added_ltrs": Union[int, float, str, None],
                    "oil_condition_rating": Union[int, float, str, None],
                },
                "wear_ppm": {
                    "iron_ppm": Union[int, float, str, None],
                    "copper_ppm": Union[int, float, str, None],
                    "lead_ppm": Union[int, float, str, None],
                    "molybdenum_ppm": Union[int, float, str, None],
                    "chromium_ppm": Union[int, float, str, None],
                    "nickel_ppm": Union[int, float, str, None],
                    "tin_ppm": Union[int, float, str, None],
                    "silver_ppm": Union[int, float, str, None],
                    "titanium_ppm": Union[int, float, str, None],
                    "aluminium_ppm": Union[int, float, str, None],
                    "antimony_ppm": Union[int, float, str, None],
                },
                "contamination": {
                    "boron_ppm": Union[int, float, str, None],
                    "silicon_ppm": Union[int, float, str, None],
                    "sodium_ppm": Union[int, float, str, None],
                    "vanadium_ppm": Union[int, float, str, None],
                    "ir_nitration_au": Union[int, float, str, None],
                    "water_percent": Union[int, float, str, None],
                },
                "particle_count": {
                    "gt_4u": Union[int, float, str, None],
                    "gt_6u": Union[int, float, str, None],
                    "gt_14u": Union[int, float, str, None],
                    "iso_code": Union[int, float, str, None],
                },
                "chemistry": {
                    "barium_ppm": Union[int, float, str, None],
                    "calcium_ppm": Union[int, float, str, None],
                    "phosphorus_ppm": Union[int, float, str, None],
                    "zinc_ppm": Union[int, float, str, None],
                    "magnesium_ppm": Union[int, float, str, None],
                    "manganese_ppm": Union[int, float, str, None],
                    "potassium_ppm": Union[int, float, str, None],
                    "ir_oxidation_au": Union[int, float, str, None],
                    "vis_40c_cst": Union[int, float, str, None],
                    "total_acid_mg_kohg": Union[int, float, str, None],
                },
            }
        ]
    },
)