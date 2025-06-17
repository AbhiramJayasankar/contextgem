from contextgem import JsonObjectConcept
from typing import Union, List

report_header_concept = JsonObjectConcept(
    name="Shell_Report_Header",
    llm_role="extractor_vision",
    description="""Extracts key customer, equipment, and diagnosis information from the top section of the Shell LubeAnalyst report.
    The diagnosis text is in a separate box.""",
    structure={
        "vessel_name": Union[str, None],
        "imo_number": Union[int, None],
        "report_provider_company": Union[int, float, str, None],
        "customer": Union[int, float, str, None],
        "site_or_vessel_name_code": Union[int, float, str, None],
        "lube_analyst_code": Union[int, float, str, None],
        "equipment_component": Union[int, float, str, None],
        "manufacturer": Union[int, float, str, None],
        "model": Union[int, float, str, None],
        "registered_lubricant": Union[int, float, str, None],
        "diagnosis": {
            "status": Union[int, float, str, None],
            "remarks": Union[int, float, str, None],
        },
    },
)

oil_analysis_results_concept = JsonObjectConcept(
    name="Shell_Analysis_Results",
    llm_role="extractor_vision",
    description="""Each column under 'Sample Information' is a separate sample; extract the data for each one.
    Some rows in the table contain multiple test results (e.g., Flash Point and TBN are on the same line). Extract each value to its corresponding field.
    Leave empty cells as null.""",
    add_justifications=False,
    add_references=False,
    singular_occurrence=False,
    justification_depth="brief",
    justification_max_sents=2,
    structure={
        "samples": [
            {
                "sample_details": {
                    "sample_number": Union[int, float, str, None],
                    "sample_condition": Union[int, float, str, None],
                    "sample_date": Union[int, float, str, None],
                    "sample_received": Union[int, float, str, None],
                    "sample_completed": Union[int, float, str, None],
                },
                "usage_information": {
                    "lubricant_in_use": Union[int, float, str, None],
                    "equipment_life_hours": Union[int, float, str, None],
                    "lubricant_life_hours": Union[int, float, str, None],
                    "top_up_volume_litres": Union[int, float, str, None],
                    "fuel_used": Union[int, float, str, None],
                },
                "physical_characteristics": {
                    "viscosity_100c_cst": Union[int, float, str, None],
                    "flash_point_setaflash_c": Union[int, float, str, None],
                    "tbn_d2896_mg_koh_g": Union[int, float, str, None],
                },
                "wear_analysis": {
                    "iron_fe_ppm": Union[int, float, str, None],
                    "chromium_cr_ppm": Union[int, float, str, None],
                    "tin_sn_ppm": Union[int, float, str, None],
                    "lead_pb_ppm": Union[int, float, str, None],
                    "copper_cu_ppm": Union[int, float, str, None],
                    "aluminium_al_ppm": Union[int, float, str, None],
                    "vanadium_v_ppm": Union[int, float, str, None],
                    "wpi_index": Union[int, float, str, None],
                },
                "contamination_analysis": {
                    "water_content_percent": Union[int, float, str, None],
                    "index_of_contamination_ic_percent": Union[int, float, str, None],
                    "merit_of_dispersancy_md": Union[int, float, str, None],
                    "demerit_point_dp": Union[int, float, str, None],
                    "sodium_na_ppm": Union[int, float, str, None],
                    "silicon_si_ppm": Union[int, float, str, None],
                },
                "additive_analysis": {
                    "calcium_ca_percent": Union[int, float, str, None],
                    "zinc_zn_percent": Union[int, float, str, None],
                    "phosphorus_p_percent": Union[int, float, str, None],
                    "barium_ba_percent": Union[int, float, str, None],
                    "molybdenum_mo_ppm": Union[int, float, str, None],
                    "magnesium_mg_ppm": Union[int, float, str, None],
                    "boron_b_ppm": Union[int, float, str, None],
                },
            }
        ],
    },
)