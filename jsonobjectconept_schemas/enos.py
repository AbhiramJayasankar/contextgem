from contextgem import JsonObjectConcept
from typing import Union, List

report_header_concept = JsonObjectConcept(
    name="Eneos_Report_Header",
    llm_role="extractor_vision",
    description="""Extracts key customer and equipment information from the top section of the ENEOS oil analysis report.
    Some sections names and the data are seperated by a lot of whitespace.
    Identify empty sections and leave blank""",
    structure={
        "report_provider_company": Union[int, float, str, None],
        "report_id": Union[int, float, str, None],
        "equipment_information": {
            "company_name": Union[int, float, str, None],
            "vessel_name": Union[str, None],
            "imo_number": Union[int, None],
            "oilgrade_in_use": Union[int, float, str, None],
            "equipment_make": Union[int, float, str, None],
            "equipment_model": Union[int, float, str, None],
            "machinery_unit": Union[int, float, str, None],
            "sample_location": Union[int, float, str, None],
        }
    },
)

oil_analysis_results_concept = JsonObjectConcept(
    name="Eneos_Analysis_Results",
    llm_role="extractor_vision",
    description="""Each column in the results table is a separate sample; extract the data for each. 
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
                    "oilgrade_in_use": Union[int, float, str, None],
                    "fuel_used": Union[int, float, str, None],
                    "equipment_life_h": Union[int, float, str, None],
                    "oil_life_h": Union[int, float, str, None],
                    "oil_added_l": Union[int, float, str, None],
                    "lubricant_condition": Union[int, float, str, None],
                },
                "oil_analysis": {
                    "viscosity_40c_mm2_s": Union[int, float, str, None],
                    "astm_color": Union[int, float, str, None],
                    "total_acid_number_mg_koh_g": Union[int, float, str, None],
                    "water_content_percent_w": Union[int, float, str, None],
                    "chloride_nature_of_water": Union[int, float, str, None],
                },
                "element_analysis_ppm": {
                    "iron_fe_ppm": Union[int, float, str, None],
                    "chromium_cr_ppm": Union[int, float, str, None],
                    "molybdenum_mo_ppm": Union[int, float, str, None],
                    "copper_cu_ppm": Union[int, float, str, None],
                    "lead_pb_ppm": Union[int, float, str, None],
                    "silver_ag_ppm": Union[int, float, str, None],
                    "tin_sn_ppm": Union[int, float, str, None],
                    "aluminnium_al_ppm": Union[int, float, str, None],
                    "nickel_ni_ppm": Union[int, float, str, None],
                    "vanadium_v_ppm": Union[int, float, str, None],
                    "silicon_si_ppm": Union[int, float, str, None],
                    "boron_b_ppm": Union[int, float, str, None],
                    "sodium_na_ppm": Union[int, float, str, None],
                    "magnesium_mg_ppm": Union[int, float, str, None],
                    "phosphorus_p_ppm": Union[int, float, str, None],
                    "zinc_zn_ppm": Union[int, float, str, None],
                    "barium_ba_ppm": Union[int, float, str, None],
                    "calcium_ca_ppm": Union[int, float, str, None],
                    "potassium_k_ppm": Union[int, float, str, None],
                    "titanium_ti_ppm": Union[int, float, str, None],
                    "manganese_mn_ppm": Union[int, float, str, None],
                    "lithium_li_ppm": Union[int, float, str, None],
                    "cadmium_cd_ppm": Union[int, float, str, None],
                },
            }
        ],
        "diagnosis_remarks": {
            "remarks": Union[int, float, str, None],
        }
    },
)