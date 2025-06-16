from contextgem import JsonObjectConcept
from typing import Union, List

report_header_concept = JsonObjectConcept(
    name="Lubmarine_Report_Header",
    llm_role="extractor_vision",
    description="Extracts key vessel, oil, and lab information from the top section of the Lubmarine report.",
    structure={
        "report_provider_company": Union[int, float, str, None],
        "overall_lubricant_condition": Union[int, float, str, None],
        "equipment_information": {
            "vessel_name": Union[str, None],
            "vessel_imo": Union[int, None],
            "company": Union[int, float, str, None],
            "unit_name": Union[int, float, str, None],
            "unit_id": Union[int, float, str, None],
            "description": Union[int, float, str, None],
            "make": Union[int, float, str, None],
            "model": Union[int, float, str, None],
            "oil_type": Union[int, float, str, None],
            "sample_no": Union[int, float, str, None],
            "analysis_no": Union[int, float, str, None],
            "reported": Union[int, float, str, None],
            "affiliate": Union[int, float, str, None],
            "lab": Union[int, float, str, None],
        }
    },
)

oil_analysis_results_concept = JsonObjectConcept(
    name="Lubmarine_Analysis_Results",
    llm_role="extractor_vision",
    description="""Each column in the DATA table is a separate sample; extract the data for each.
    The Symptoms and Comments should be extracted into the summary object.
    Leave empty cells as null.""",
    add_justifications=False,
    add_references=False,
    singular_occurrence=False,
    justification_depth="brief",
    justification_max_sents=2,
    structure={
        "summary": {
            "symptoms": Union[int, float, str, None],
            "comments": Union[int, float, str, None],
        },
        "samples": [
            {
                "sample_data": {
                    "status": Union[int, float, str, None],
                    "sample_no": Union[int, float, str, None],
                    "date_sampled": Union[int, float, str, None],
                    "date_recieved": Union[int, float, str, None],
                    "port_landed": Union[int, float, str, None],
                    "oil_on_label": Union[int, float, str, None],
                    "purifier_filter": Union[int, float, str, None],
                    "equipment_life": Union[int, float, str, None],
                    "oil_life": Union[int, float, str, None],
                    "top_up_volume": Union[int, float, str, None],
                },
                "analysis": {
                    "visco_40c_mm2s": Union[int, float, str, None],
                    "visco_100c_mm2s": Union[int, float, str, None],
                    "acid_number_mg_kohg": Union[int, float, str, None],
                    "water_content_percent_mass": Union[int, float, str, None],
                    "Chlorides": Union[int, float, str, None],
                    "pq_index": Union[int, float, str, None],
                    "oxidation_by_ftir_abs_cm": Union[int, float, str, None],
                },
                "spectro_analysis": {
                    "wear_elements": {
                        "iron_fe": Union[int, float, str, None],
                        "chromium_cr": Union[int, float, str, None],
                        "molybdenum_mo": Union[int, float, str, None],
                        "copper_cu": Union[int, float, str, None],
                        "lead_pb": Union[int, float, str, None],
                        "silver_ag": Union[int, float, str, None],
                        "tin_sn": Union[int, float, str, None],
                        "aluminum_al": Union[int, float, str, None],
                    },
                    "contaminants": {
                        "nickel_ni": Union[int, float, str, None],
                        "vanadium_v": Union[int, float, str, None],
                        "silicon_si": Union[int, float, str, None],
                        "boron_b": Union[int, float, str, None],
                        "sodium_Na": Union[int, float, str, None],
                        "magnesium_mg": Union[int, float, str, None],
                    },
                    "other_metals": {
                        "phosphorus_p": Union[int, float, str, None],
                        "zinc_zn": Union[int, float, str, None],
                        "barium_ba": Union[int, float, str, None],
                        "calcium_ca": Union[int, float, str, None],
                        "magnesium_mg": Union[int, float, str, None]
                    },
                },
            }
        ],
    },
)