from contextgem import JsonObjectConcept
from typing import Union, List

# Schema for extracting header, footer, and general report information
report_header_concept = JsonObjectConcept(
    name="NOF Report Metadata",
    llm_role="extractor_vision",
    description="Extract key header, footer, and summary information from the NOF Corporation oil analysis report.",
    structure={
        "report_provider_details": {
            "report_provider_company": Union[int, float, str, None],
            "report_date": Union[int, float, str, None],
            "office_name": Union[int, float, str, None],
            "contact_person": Union[int, float, str, None],
        },
        "customer_details": {
            "customer_name": Union[int, float, str, None],
            "customer_address": Union[int, float, str, None],
        },
        "asset_details": {
            "vessel": Union[str, None],
            "imo_number": Union[int, None],
        },
        "overall_condition": Union[int, float, str, None],
        "critical_value_note": Union[int, float, str, None],
        "comment": Union[int, float, str, None],
        "provider_footer_details": {
            "address": Union[int, float, str, None],
            "tel": Union[int, float, str, None],
            "fax": Union[int, float, str, None],
        },
    },
)

# Schema for extracting the detailed results from the main table
oil_analysis_results_concept = JsonObjectConcept(
    name="NOF Report Results",
    llm_role="extractor_vision",
    description="Extract the detailed test results and critical values from the main results table.",
    singular_occurrence=False,
    structure={
        "samples": [
            {
                "sample_details": {
                    "sample_number": Union[int, float, str, None],
                    "machinery": Union[int, float, str, None],
                    "product": Union[int, float, str, None],
                    "date_sampled": Union[int, float, str, None],
                    "running_time_since_last_oil_change_hrs": Union[int, float, str, None],
                },
                "oil_properties": {
                    "kv_at_40c_mm2s": Union[int, float, str, None],
                    "acid_number_mg_koh_g": Union[int, float, str, None],
                    "water_mass_percent": Union[int, float, str, None],
                },
                "elements_mass_ppm": {
                    "iron_fe": Union[int, float, str, None],
                    "lead_pb": Union[int, float, str, None],
                    "copper_cu": Union[int, float, str, None],
                    "chromium_cr": Union[int, float, str, None],
                    "aluminium_al": Union[int, float, str, None],
                    "nickel_ni": Union[int, float, str, None],
                    "silver_ag": Union[int, float, str, None],
                    "tin_sn": Union[int, float, str, None],
                    "silicon_si": Union[int, float, str, None],
                    "boron_b": Union[int, float, str, None],
                    "sodium_na": Union[int, float, str, None],
                    "phosphorus_p": Union[int, float, str, None],
                    "zinc_zn": Union[int, float, str, None],
                    "calcium_ca": Union[int, float, str, None],
                    "barium_ba": Union[int, float, str, None],
                    "magnesium_mg": Union[int, float, str, None],
                    "molybdenum_mo": Union[int, float, str, None],
                }
            }
        ]
    },
)