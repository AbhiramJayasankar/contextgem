from contextgem import JsonObjectConcept
from typing import Union, List

report_header_concept = JsonObjectConcept(
    name="Gulf_Lubricant_Report_Header",
    llm_role="extractor_vision",
    description="Extracts key customer and equipment information from the top section of the Gulf Lubricant Condition report.",
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

oil_analysis_results_concept = JsonObjectConcept(
    name="Gulf_Lubricant_Analysis_Results",
    llm_role="extractor_vision",
    description="""Each column in the results table is a separate sample; extract the data for each.
    The recommendation at the bottom should be extracted into the recommendations object.
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
                    "sample_no": Union[int, float, str, None],
                    "bottle_no": Union[int, float, str, None],
                    "date_received": Union[int, float, str, None],
                    "sampled_date": Union[int, float, str, None],
                    "port_of_landing": Union[int, float, str, None],
                    "oil_on_label": Union[int, float, str, None],
                    "fuel_in_use_sulphur_percent": Union[int, float, str, None],
                    "total_frame_running_hours": Union[int, float, str, None],
                    "lubricant_hours": Union[int, float, str, None],
                    "lubricant_condition": Union[int, float, str, None],
                },
                "analysis": {
                    "viscosity_cst_mm2_s": Union[int, float, str, None],
                    "viscosity_index": Union[int, float, str, None],
                    "water_percent_wt": Union[int, float, str, None],
                    "an_mgkoh_g": Union[int, float, str, None],
                    "pq_index_2ml": Union[int, float, str, None],
                    "iso_code": Union[int, float, str, None],
                    "greater_than_4_um": Union[int, float, str, None],
                    "greater_than_6_um": Union[int, float, str, None],
                    "greater_than_14_um": Union[int, float, str, None],
                },
                "wear_elements_ppm": {
                    "aluminum_al_ppm": Union[int, float, str, None],
                    "chromium_cr_ppm": Union[int, float, str, None],
                    "copper_cu_ppm": Union[int, float, str, None],
                    "iron_fe_ppm": Union[int, float, str, None],
                    "lead_pb_ppm": Union[int, float, str, None],
                    "tin_sn_ppm": Union[int, float, str, None],
                },
                "other_elements_ppm": {
                    "boron_b_ppm": Union[int, float, str, None],
                    "sodium_na_ppm": Union[int, float, str, None],
                    "silicon_si_ppm": Union[int, float, str, None],
                    "molybdenum_mo_ppm": Union[int, float, str, None],
                    "nickel_ni_ppm": Union[int, float, str, None],
                    "silver_ag_ppm": Union[int, float, str, None],
                    "vanadium_v_ppm": Union[int, float, str, None],
                    "lithium_li_ppm": Union[int, float, str, None],
                    "barium_ba_ppm": Union[int, float, str, None],
                },
            }
        ],
        "recommendations": {
            "text": Union[int, float, str, None],
        }
    },
)