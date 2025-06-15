from contextgem import JsonObjectConcept
from typing import Union, List

report_header_concept = JsonObjectConcept(
    name="Condition_Monitoring_Report_Header",
    llm_role="extractor_vision",
    description="Extract key identification and metadata from the top section of the condition monitoring report.",
    structure={
        "report_provider_company": Union[int, float, str, None],
        "vessel": Union[str, None],
        "imo": Union[int, None],
        "customer": Union[int, float, str, None],
        "system": Union[int, float, str, None],
        "date_reported": Union[int, float, str, None],
        "overall_status": Union[int, float, str, None],
    },
)

oil_analysis_results_concept = JsonObjectConcept(
    name="Condition_Monitoring_Analysis_Results",
    llm_role="extractor_vision",
    description="""Each column in the results table is a separate sample; extract the data for each sample.
    The summary information at the bottom should be extracted into the summary object.
    Leave empty cells as null.""",
    add_justifications=False,
    add_references=False,
    singular_occurrence=False,
    justification_depth="brief",
    justification_max_sents=2,
    structure={
        "samples": [
            {
                "sample_logistics": {
                    "request_no": Union[int, float, str, None],
                    "alternate_request_no": Union[int, float, str, None],
                    "product": Union[int, float, str, None],
                    "port": Union[int, float, str, None],
                    "date_sampled": Union[int, float, str, None],
                    "date_landed": Union[int, float, str, None],
                    "date_reported": Union[int, float, str, None],
                    "product_service_hrs": Union[int, float, str, None],
                    "total_equipment_hrs": Union[int, float, str, None],
                    "consumption_l_d": Union[int, float, str, None],
                },
                "condition_and_analysis": {
                    "status_indicator": Union[int, float, str, None],
                    "appearance": Union[int, float, str, None],
                    "water_content_percent": Union[int, float, str, None],
                    "kin_viscosity_40C_cst": Union[int, float, str, None],
                    "total_acid_number_mgkoh_g": Union[int, float, str, None],
                },
                "spectrographic_analysis_ppm": {
                    "calcium_ppm": Union[int, float, str, None],
                    "zinc_ppm": Union[int, float, str, None],
                    "phosphorus_ppm": Union[int, float, str, None],
                    "molybdenum_ppm": Union[int, float, str, None],
                    "iron_ppm": Union[int, float, str, None],
                    "copper_ppm": Union[int, float, str, None],
                    "lead_ppm": Union[int, float, str, None],
                    "chromium_ppm": Union[int, float, str, None],
                    "aluminum_ppm": Union[int, float, str, None],
                    "silicon_ppm": Union[int, float, str, None],
                    "tin_ppm": Union[int, float, str, None],
                    "nickel_ppm": Union[int, float, str, None],
                    "vanadium_ppm": Union[int, float, str, None],
                },
            }
        ],
        "summary": {
            "latest_comments_request_no": Union[int, float, str, None],
            "product_given_as": Union[int, float, str, None],
            "sample_request_number_details": Union[int, float, str, None],
            "final_recommendation": Union[int, float, str, None],
        }
    },
)