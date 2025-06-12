from contextgem import JsonObjectConcept
from typing import Union

# Schema for extracting header, summary, and general equipment details
report_header_concept = JsonObjectConcept(
    name="VPS Report Metadata",
    llm_role="extractor_vision",
    description="Extract key header information, summary statement, and general equipment details from the VPS report.",
    structure={
        "report_provider_company": Union[int, float, str, None],
        "vessel_name": Union[int, float, str, None],
        "vessel_imo": Union[int, float, str, None],
        "part_name": Union[int, float, str, None],
        "summary_statement": Union[int, float, str, None],
        "sample_details": {
            "manufacturer": Union[int, float, str, None],
            "oil_brand": Union[int, float, str, None],
            "vps_equipment_id_no": Union[int, float, str, None],
            "model": Union[int, float, str, None],
            "oil_quantity_in_system_litres": Union[int, float, str, None],
        },
    },
)

# Schema for extracting the detailed results from each sample column
oil_analysis_results_concept = JsonObjectConcept(
    name="VPS Report Results",
    llm_role="extractor_vision",
    description="Extract the test results for each sample column. Each column, including current and previous, is a separate sample.",
    singular_occurrence=False,
    structure={
        "samples": [
            {
                "test_results": {
                    "sample_column_type": Union[int, float, str, None],  # e.g., "Current" or "Previous Samples"
                    "sample_number": Union[int, float, str, None],
                    "rating": Union[int, float, str, None],
                    "sampling_date": Union[int, float, str, None],
                    "sampling_point": Union[int, float, str, None],
                    "unit_service_hrs": Union[int, float, str, None],
                    "oil_service_hrs": Union[int, float, str, None],
                    "oil_top_up_volume_daily": Union[int, float, str, None],
                    "lube_grade": Union[int, float, str, None],
                    "fuel_in_use": Union[int, float, str, None],

                },
                "lubricant_data": {
                    "viscosity_at_40c": Union[int, float, str, None],
                    "viscosity_at_100c": Union[int, float, str, None],
                    "viscosity_index": Union[int, float, str, None],
                    "oxidation": Union[int, float, str, None],
                    "acid_number": Union[int, float, str, None],
                },
                "wear": {
                    "aluminium": Union[int, float, str, None],
                    "iron": Union[int, float, str, None],
                    "lead": Union[int, float, str, None],
                    "silver": Union[int, float, str, None],
                    "chromium": Union[int, float, str, None],
                    "copper": Union[int, float, str, None],
                    "molybdenum": Union[int, float, str, None],
                    "titanium": Union[int, float, str, None],
                    "manganese": Union[int, float, str, None],
                },
                "contaminants": {
                    "water": Union[int, float, str, None],
                    "vanadium": Union[int, float, str, None],
                    "sodium": Union[int, float, str, None],
                    "silicon": Union[int, float, str, None],
                    "nickel": Union[int, float, str, None],
                    "potassium": Union[int, float, str, None],
                    "particle_count_4_micron_c": Union[int, float, str, None],
                    "particle_count_6_micron_c": Union[int, float, str, None],
                    "particle_count_14_micron_c": Union[int, float, str, None],
                    "iso_4406_code_number": Union[int, float, str, None],
                },
                "additives_ppm": {
                    "calcium": Union[int, float, str, None],
                    "magnesium": Union[int, float, str, None],
                    "zinc": Union[int, float, str, None],
                    "phosphorus": Union[int, float, str, None],
                    "lithium": Union[int, float, str, None],
                    "cadmium": Union[int, float, str, None],
                    "antimony": Union[int, float, str, None],
                    "boron": Union[int, float, str, None],
                    "barium": Union[int, float, str, None],
                },
            }
        ]
    },
)