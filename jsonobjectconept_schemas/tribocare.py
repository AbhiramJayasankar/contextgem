from contextgem import JsonObjectConcept
from typing import Union, List

report_header_concept = JsonObjectConcept(
    name="Tribocare Report Metadata",
    llm_role="extractor_vision",
    description="Extract key identification, metadata, and summary comments from the oil analysis report.",
    structure={
        "report_provider_company": Union[int, float, str, None],
        "customer_name": Union[int, float, str, None],
        "vessel_name": Union[str, None],
        "vessel_imo": Union[int, None],
        "machinery_name": Union[int, float, str, None],
        "manufacturer_details": {
            "manufacturer": Union[int, float, str, None],
            "port_landed": Union[int, float, str, None],
            "model": Union[int, float, str, None],
            "volume_ltr": Union[int, float, str, None],
        },
        "product_information": {
            "recommended_product": Union[int, float, str, None],
            "fuel_grade_or_type": Union[int, float, str, None],
        },
        "logistics": {
            "dispatched_date": Union[int, float, str, None],
            "received_date": Union[int, float, str, None],
        },
        "report_summary": {
            "oil_rating_comment": Union[int, float, str, None],
            "unit_rating_comment": Union[int, float, str, None],
            "action_required": Union[int, float, str, None],
            "critical_value_note": Union[int, float, str, None],
        }
    },
)

oil_analysis_results_concept = JsonObjectConcept(
    name="Tribocare Oil Analysis Results",
    llm_role="extractor_vision",
    description="Extract the test results for each sample column. Each column in the results table is a separate sample.",
    singular_occurrence=False,
    structure={
        "samples": [
            {
                "sample_details": {
                    "rating": Union[int, float, str, None],
                    "sample_no": Union[int, float, str, None],
                    "bottle_no": Union[int, float, str, None],
                    "sampled_date": Union[int, float, str, None],
                    "oil_grade_in_use": Union[int, float, str, None],
                    "unit_service_hrs": Union[int, float, str, None],
                    "oil_service_hrs": Union[int, float, str, None],
                    "daily_makeup_l": Union[int, float, str, None],
                },
                "analysis": {
                    "appearance": Union[int, float, str, None],
                    "kv_at_40c_mm2s": Union[int, float, str, None],
                    "water_percent_vol": Union[int, float, str, None],
                    "soot_insol_percent_wt": Union[int, float, str, None],
                    "oxidation_abs_0_1mm": Union[int, float, str, None],
                    "an_mgkoh_g": Union[int, float, str, None],
                    "chloride_cl_ppm": Union[int, float, str, None],
                    "pq_index_2ml": Union[int, float, str, None],
                },
                "wear_elements_ppm": {
                    "chromium_cr": Union[int, float, str, None],
                    "copper_cu": Union[int, float, str, None],
                    "iron_fe": Union[int, float, str, None],
                    "lead_pb": Union[int, float, str, None],
                    "tin_sn": Union[int, float, str, None],
                    "nickel_ni": Union[int, float, str, None],
                    "antimony_sb": Union[int, float, str, None],
                },
                "contaminant_elements_ppm": {
                    "boron_b": Union[int, float, str, None],
                    "sodium_na": Union[int, float, str, None],
                    "magnesium_mg": Union[int, float, str, None],
                    "silicon_si": Union[int, float, str, None],
                },
                "additive_elements_ppm": {
                    "calcium_ca": Union[int, float, str, None],
                    "zinc_zn": Union[int, float, str, None],
                    "phosphorus_p": Union[int, float, str, None],
                    "magnesium_mg": Union[int, float, str, None]
                },
            }
        ]
    },
)