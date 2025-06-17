from contextgem import JsonObjectConcept
from typing import Union, List

report_header_concept = JsonObjectConcept(
    name="Maritec_Report_Header",
    llm_role="extractor_vision",
    description="""Extracts key recipient and equipment information from the header of the Maritec oil analysis report.""",
    structure={
        "report_provider": Union[int, float, str, None],
        "recipient_company": Union[int, float, str, None],
        "recipient_department": Union[int, float, str, None],
        "vessel_imo": Union[int, float, str, None],
        "component": Union[int, float, str, None],
    },
)

oil_analysis_results_concept = JsonObjectConcept(
    name="Maritec_Analysis_Results",
    llm_role="extractor_vision",
    description="""Each column with a 'Report Number' is a separate sample; extract the data for each one.
    The 'REMARKS' at the bottom of the page should be extracted into the remarks object.
    Leave empty cells or cells with 'Not Stated' as null.""",
    add_justifications=False,
    add_references=False,
    singular_occurrence=False,
    justification_depth="brief",
    justification_max_sents=2,
    structure={
        "samples": [
            {
                "sample_metadata": {
                    "status": Union[int, float, str, None],
                    "report_number": Union[int, float, str, None],
                    "report_date": Union[int, float, str, None],
                    "equipment_hours": Union[int, float, str, None],
                    "oil_service_hours": Union[int, float, str, None],
                    "oil_volume_litres": Union[int, float, str, None],
                    "oil_brand_grade": Union[int, float, str, None],
                    "sampling_location": Union[int, float, str, None],
                    "sampling_date": Union[int, float, str, None],
                    "sent_from": Union[int, float, str, None],
                    "date_sent": Union[int, float, str, None],
                    "received_date": Union[int, float, str, None],
                },
                "lube_oil_properties": {
                    "kv40_cst": Union[int, float, str, None],
                    "kv100_cst": Union[int, float, str, None],
                    "viscosity_index": Union[int, float, str, None],
                    "acid_number_mgkoh_g": Union[int, float, str, None],
                    "base_number_mgkoh_g": Union[int, float, str, None],
                    "water_crackle_percent_wt": Union[int, float, str, None],
                    "water_content_percent_w": Union[int, float, str, None],
                    "flash_point_pmcc_deg_c": Union[int, float, str, None],
                    "pentane_insolubles_percent_wt": Union[int, float, str, None],
                },
                "spectrometric_analysis_mg_kg": {
                    "iron": Union[int, float, str, None],
                    "lead": Union[int, float, str, None],
                    "copper": Union[int, float, str, None],
                    "chromium": Union[int, float, str, None],
                    "aluminium": Union[int, float, str, None],
                    "nickel": Union[int, float, str, None],
                    "silver": Union[int, float, str, None],
                    "tin": Union[int, float, str, None],
                    "silicon": Union[int, float, str, None],
                    "boron": Union[int, float, str, None],
                    "sodium": Union[int, float, str, None],
                    "phosphorus": Union[int, float, str, None],
                    "zinc": Union[int, float, str, None],
                    "calcium": Union[int, float, str, None],
                    "barium": Union[int, float, str, None],
                    "magnesium": Union[int, float, str, None],
                    "vanadium": Union[int, float, str, None],
                    "molybdenum": Union[int, float, str, None],
                },
            }
        ],
        "remarks": {
            "subject": Union[int, float, str, None],
            "comment": Union[int, float, str, None],
            "external_lab_reference": Union[int, float, str, None],
        },
    },
)