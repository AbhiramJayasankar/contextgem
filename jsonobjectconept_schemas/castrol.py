from contextgem import JsonObjectConcept
from typing import Union

# This header concept is compatible with both report styles.
report_header_concept = JsonObjectConcept(
    name="Oil Analysis Report Header",
    llm_role="extractor_vision",
    description="Extract key identification and metadata from the top section of the oil analysis report.",
    structure={
        "report_provider_company": Union[int, float, str, None],
        "customer_name": Union[int, float, str, None],
        "asset_details": {
            "vessel_or_asset": Union[int, float, str, None],
            "imo_or_asset_number": Union[int, float, str, None],
            "machinery_description": Union[int, float, str, None],
            "manufacturer": Union[int, float, str, None],
            "model": Union[int, float, str, None],
        },
        "sample_identification": {
            "sample_number": Union[int, float, str, None],
            "customer_sample_point_id": Union[int, float, str, None],
            "sampling_point": Union[int, float, str, None],
            "sample_number": Union[int, float, str, None],
            "sample_label_ref": Union[int, float, str, None],
            "label_sampling_point": Union[int, float, str, None],
        },
        "product_information": {
            "model": Union[int, float, str, None],
            "product_in_use_uoa_schedule": Union[int, float, str, None],
        },
        "logistics": {
            "port_landed": Union[int, float, str, None],
            "contact_email": Union[int, float, str, None],
        },
        "diagnosis_summary": {
            "diagnosed_by": Union[int, float, str, None],
            "diagnosis": Union[int, float, str, None],
        }
    },
)

# This results concept is a superset of the fields in both reports.
oil_analysis_results_concept = JsonObjectConcept(
    name="Oil Analysis Sample Results",
    llm_role="extractor_vision",
    description="""Each column in results is a separate section; do not mix them up.
    Extract the test results for each sample column in the results section.
    This schema is a superset of multiple report formats. Leave empty or non-existent cells as an empty string.""",
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
                    "historic_sample_number": Union[int, float, str, None],
                    "sampling_date": Union[int, float, str, None],
                    "date_received": Union[int, float, str, None],
                    "date_reported": Union[int, float, str, None],
                    "oil_life_hrs": Union[int, float, str, None],
                    "equipment_life_hrs": Union[int, float, str, None],
                    "status_rating": Union[int, float, str, None],
                },
                "standard_tests": {
                    "appearance": Union[int, float, str, None],
                    "color": Union[int, float, str, None],
                    "free_water_percent": Union[int, float, str, None],
                    "water_content_percent": Union[int, float, str, None],
                    "flash_point_at_190C": Union[int, float, str, None],
                    "viscosity_40C_cst": Union[int, float, str, None],
                    "viscosity_100C_cst": Union[int, float, str, None],
                    "insolubles_percent": Union[int, float, str, None],
                    "an_mg_koh_g": Union[int, float, str, None],
                    "bn_mg_koh_g": Union[int, float, str, None],
                    "san_astm_d664_mg_koh_g": Union[int, float, str, None],
                },
                "spectrometry_ppm": {
                    "ag_silver_ppm": Union[int, float, str, None],
                    "al_aluminium_ppm": Union[int, float, str, None],
                    "b_boron_ppm": Union[int, float, str, None],
                    "ca_calcium_ppm": Union[int, float, str, None],
                    "cr_chromium_ppm": Union[int, float, str, None],
                    "cu_copper_ppm": Union[int, float, str, None],
                    "fe_iron_ppm": Union[int, float, str, None],
                    "mg_magnesium_ppm": Union[int, float, str, None],
                    "mo_molybdenum_ppm": Union[int, float, str, None],
                    "na_sodium_ppm": Union[int, float, str, None],
                    "ni_nickel_ppm": Union[int, float, str, None],
                    "p_phosphorus_ppm": Union[int, float, str, None],
                    "pb_lead_ppm": Union[int, float, str, None],
                    "sb_antimony_ppm": Union[int, float, str, None],
                    "si_silicon_ppm": Union[int, float, str, None],
                    "sn_tin_ppm": Union[int, float, str, None],
                    "v_vanadium_ppm": Union[int, float, str, None],
                    "ti_titanium_ppm": Union[int, float, str, None],
                    "zn_zinc_ppm": Union[int, float, str, None],
                },
            }
        ]
    },
)