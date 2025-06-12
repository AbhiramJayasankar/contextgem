from contextgem import JsonObjectConcept
from typing import Union, List

# Schema for extracting high-level metadata from the report
report_header_concept = JsonObjectConcept(
    name="Mobil Serv Report Metadata",
    llm_role="extractor_vision",
    description="Extract key header, account, equipment, and summary information from the Mobil Serv report.",
    singular_occurrence=True,

    structure={
        "report_provider_company": Union[int, float, str, None],
        "report_status": Union[int, float, str, None],
        "unit_id": Union[int, float, str, None],
        "asset_id": Union[int, float, str, None],
        "description": Union[int, float, str, None],
        "account_information": {
            "id": Union[int, float, str, None],
            "name": Union[int, float, str, None],
            "imo_reg_number": Union[int, float, str, None],
            "parent_account": Union[int, float, str, None],
        },
        "sample_information": {
            "sample_id": Union[int, float, str, None],
            "service_level": Union[int, float, str, None],
            "bottle_id": Union[int, float, str, None],
            "tested_lubricant": Union[int, float, str, None],
        },
        "equipment_information": {
            "asset_class": Union[int, float, str, None],
            "manufacturer": Union[int, float, str, None],
            "model": Union[int, float, str, None],
            "lubricant": Union[int, float, str, None],
        },
        "recommendation_comments": Union[int, float, str, None],
        "sample_timeline": List[Union[int, float, str, None]],
    },
)

# Schema for extracting detailed results from the sample columns
oil_analysis_results_concept = JsonObjectConcept(
    name="Mobil Serv Report Results",
    llm_role="extractor_vision",
    description="Extract the detailed test results for each sample column from the main data table spanning both pages.",
    singular_occurrence=False,
    structure={
        "samples": [
            {
                "report_column_status": Union[int, float, str, None],
                "sample_id": Union[int, float, str, None],
                "service_level": Union[int, float, str, None],
                "sample_info": {
                    "bottle_id": Union[int, float, str, None],
                    "tested_lubricant": Union[int, float, str, None],
                    "sampled_date": Union[int, float, str, None],
                    "reported_date": Union[int, float, str, None],
                    "hrs_since_last_overhaul": Union[int, float, str, None],
                    "oil_service_hours": Union[int, float, str, None],
                    "used_oil_volume": Union[int, float, str, None],
                    "used_oil_volume_UOM": Union[int, float, str, None],
                    "oil_used_in_last_24_hrs": Union[int, float, str, None],
                    "oil_used_in_last_24_hrs_UOM": Union[int, float, str, None],
                    "port_landed": Union[int, float, str, None],
                    "date_landed": Union[int, float, str, None],
                    "total_equipment_hours": Union[int, float, str, None],
                },
                "lubricant_properties": {
                    "dac_percent_asphalt": Union[int, float, str, None],
                    "contamination_rating": Union[int, float, str, None],
                    "equipment_rating": Union[int, float, str, None],
                    "lubricant_rating": Union[int, float, str, None],
                    "pq_index": Union[int, float, str, None],
                    "visc_at_100c_cst": Union[int, float, str, None],
                    "oxidation_ab_cm": Union[int, float, str, None],
                    "tbn_mg_koh_g": Union[int, float, str, None],
                    "soot_wt_percent": Union[int, float, str, None],
                    "water_vol_percent": Union[int, float, str, None],
                    "coolant_indicator": Union[int, float, str, None],
                },
                "wear_ppm": {
                    "ag_silver": Union[int, float, str, None],
                    "al_aluminium": Union[int, float, str, None],
                    "cr_chromium": Union[int, float, str, None],
                    "cu_copper": Union[int, float, str, None],
                    "fe_iron": Union[int, float, str, None],
                    "mo_molybdenum": Union[int, float, str, None],
                    "ni_nickel": Union[int, float, str, None],
                    "pb_lead": Union[int, float, str, None],
                    "sn_tin": Union[int, float, str, None],
                },
                "contaminants_ppm": {
                    "k_potassium": Union[int, float, str, None],
                    "na_sodium": Union[int, float, str, None],
                    "si_silicon": Union[int, float, str, None],
                    "v_vanadium": Union[int, float, str, None],
                },
                
            }
        ]
    },
)