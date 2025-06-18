castrol_field_map = {
    "testLab": "Castrol",

"LatestLatestSampleIdentification":{
    "sampleNumber": "report_header.sample_identification.sample_number",
    "bottleNumber": "report_header.sample_identification.sample_label_ref",
    "analysisNumber": None},

  "VesselAndEquipmentInformation": {
    "testLabExtracted": "report_header.report_provider_company",
    "vesselNameExtracted": "report_header.asset_details.vessel_or_asset",
    "imoExtracted": "report_header.asset_details.imo_or_asset_number",
    "customerCompany": "report_header.customer_name",
    "machineryName": "report_header.asset_details.machinery_description",
    "equipmentMake": "report_header.asset_details.manufacturer",
    "equipmentModel": "report_header.asset_details.model",
    "equipmentSerial": None,
    "sampleLocation": "report_header.sample_identification.sampling_point",
    "machineryUnit": None,
    "portLanded": "report_header.logistics.port_landed",
    "oilGrade": "report_header.product_information.product_in_use_actual",
    "oilSystemCapacity": None,
    
  },
  "Samples": [
    {
        "sampleNumber": "oil_analysis_results.samples[].sample_details.sample_number",
        "sampleDate": "oil_analysis_results.samples[].sample_details.sampling_date",
        "dateReported": "oil_analysis_results.samples[].sample_details.date_reported",

      "OilAndOperatingConditions": {
        "oilBrand": None,
        "fuelGrade": None,
        "fuelSulfurContent": None,
        "equipmentHours": "oil_analysis_results.samples[].sample_details.equipment_life_hrs",
        "oilServiceHours": "oil_analysis_results.samples[].sample_details.oil_life_hrs",
        "oilAddedVolume": None,
        "dailyMakeupVolume": None,
        "consumptionRate": None
      },
      "PhysicalAndChemicalProperties": {
        "appearance": "oil_analysis_results.samples[].standard_tests.appearance",
        "color": "oil_analysis_results.samples[].standard_tests.color",
        "viscosity40c": "oil_analysis_results.samples[].standard_tests.viscosity_40C_cst",
        "viscosity100c": None,
        "viscosityIndex": None,
        "acidNumber": "oil_analysis_results.samples[].standard_tests.an_mg_koh_g",
        "baseNumber": None,
        "waterContent": "oil_analysis_results.samples[].standard_tests.water_content_percent",
        "freeWater": "oil_analysis_results.samples[].standard_tests.free_water_percent",
        "chlorideContent": None,
        "flashPoint": None,
        "oxidationFtir": None,
        "nitrationFtir": None,
        "sootContent": None,
        "pqIndex": None
      },
      "ParticleContamination": {
        "particles4um": None,
        "particles6um": None,
        "particles14um": None,
        "particles21um": None,
        "particles38um": None,
        "particles70um": None,
        "isoCode": None
      },
      "WearElements": {
        "iron": "oil_analysis_results.samples[].spectrometry_ppm.fe_iron_ppm",
        "copper": "oil_analysis_results.samples[].spectrometry_ppm.cu_copper_ppm",
        "lead": "oil_analysis_results.samples[].spectrometry_ppm.pb_lead_ppm",
        "tin": "oil_analysis_results.samples[].spectrometry_ppm.sn_tin_ppm",
        "aluminum": "oil_analysis_results.samples[].spectrometry_ppm.al_aluminium_ppm",
        "chromium": "oil_analysis_results.samples[].spectrometry_ppm.cr_chromium_ppm",
        "nickel": "oil_analysis_results.samples[].spectrometry_ppm.ni_nickel_ppm",
        "silver": "oil_analysis_results.samples[].spectrometry_ppm.ag_silver_ppm",
        "molybdenum": "oil_analysis_results.samples[].spectrometry_ppm.mo_molybdenum_ppm",
        "titanium": "oil_analysis_results.samples[].spectrometry_ppm.ti_titanium_ppm",
        "manganese": "oil_analysis_results.samples[].spectrometry_ppm.mn_manganese_ppm",
        "antimony": "oil_analysis_results.samples[].spectrometry_ppm.sb_antimony_ppm"
      },
      "ContaminantElements": {
        "silicon": "oil_analysis_results.samples[].spectrometry_ppm.si_silicon_ppm",
        "sodium": "oil_analysis_results.samples[].spectrometry_ppm.na_sodium_ppm",
        "potassium": None,
        "boron": "oil_analysis_results.samples[].spectrometry_ppm.b_boron_ppm",
        "vanadium": "oil_analysis_results.samples[].spectrometry_ppm.v_vanadium_ppm",
        "lithium": None,
        "cadmium": None
      },
      "AdditiveElements": {
        "calcium": "oil_analysis_results.samples[].spectrometry_ppm.ca_calcium_ppm",
        "magnesium": None,
        "zinc": None,
        "phosphorus": None,
        "barium": None
      }
    }
  ],
  "AnalysisResults": {
    "oilRating": None,
    "unitRating": None,
    "diagnosis": "report_header.diagnosis_summary.diagnosis",
    "recommendations": None,
    "actionRequired": None,
    "nextSampleDue": None,
    "sampleFrequency": None
  },
  "QualityAndCompliance": {
    "reportStatus": "oil_analysis_results.samples[0].sample_details.status_rating",
    "report ": None,
    "frequency": None,
    "dueStatus": None
  }
}


chevron_field_map = {
    "testLab": "Chevron",

"LatestSampleIdentification":{
    "sampleNumber": "oil_analysis_results.samples[-1].sample_logistics.request_no",
    "bottleNumber": None,
    "analysisNumber": None},

    "EquipmentInformation": {
        "testLabExtracted": "report_header.report_provider_company",
        "vesselNameExtracted": "report_header.vessel",
        "imoExtracted": "report_header.imo",
        "customerCompany": "report_header.customer",
        "machineryName": "report_header.system",
        "equipmentMake": None,
        "equipmentModel": None,
        "equipmentSerial": None,
        "sampleLocation": None,
        "machineryUnit": None,
        "portLanded": "oil_analysis_results.samples[1].sample_logistics.port",
        "oilGrade": "oil_analysis_results.samples[1].sample_logistics.product",
        "oilSystemCapacity": None
    },
    "Samples": [
{
        "sampleNumber": "oil_analysis_results.samples[].sample_logistics.request_no",
        "sampleDate": "oil_analysis_results.samples[].sample_logistics.date_sampled",
        "dateReported": "oil_analysis_results.samples[].sample_logistics.date_reported",

            "OilAndOperatingConditions": {
                "oilBrand": None,
                "fuelGrade": None,
                "fuelSulfurContent": None,
                "equipmentHours": "oil_analysis_results.samples[].sample_logistics.total_equipment_hrs",
                "oilServiceHours": "oil_analysis_results.samples[].sample_logistics.product_service_hrs",
                "oilAddedVolume": None,
                "dailyMakeupVolume": None,
                "consumptionRate": "oil_analysis_results.samples[].sample_logistics.consumption_l_d"
            },
            "PhysicalAndChemicalProperties": {
                "appearance": "oil_analysis_results.samples[].condition_and_analysis.appearance",
                "color": None,
                "viscosity40c": "oil_analysis_results.samples[].condition_and_analysis.kin_viscosity_40C_cst",
                "viscosity100c": None,
                "viscosityIndex": None,
                "acidNumber": "oil_analysis_results.samples[].condition_and_analysis.total_acid_number_mgkoh_g",
                "baseNumber": None,
                "waterContent": "oil_analysis_results.samples[].condition_and_analysis.water_content_percent",
                "freeWater": None,
                "chlorideContent": None,
                "flashPoint": None,
                "oxidationFtir": None,
                "nitrationFtir": None,
                "sootContent": None,
                "pqIndex": None
            },
            "ParticleContamination": {
                "particles4um": None,
                "particles6um": None,
                "particles14um": None,
                "particles21um": None,
                "particles38um": None,
                "particles70um": None,
                "isoCode": None
            },
            "WearElements": {
                "iron": "oil_analysis_results.samples[].spectrographic_analysis_ppm.iron_ppm",
                "copper": "oil_analysis_results.samples[].spectrographic_analysis_ppm.copper_ppm",
                "lead": "oil_analysis_results.samples[].spectrographic_analysis_ppm.lead_ppm",
                "tin": "oil_analysis_results.samples[].spectrographic_analysis_ppm.tin_ppm",
                "aluminum": "oil_analysis_results.samples[].spectrographic_analysis_ppm.aluminum_ppm",
                "chromium": "oil_analysis_results.samples[].spectrographic_analysis_ppm.chromium_ppm",
                "nickel": "oil_analysis_results.samples[].spectrographic_analysis_ppm.nickel_ppm",
                "silver": None,
                "molybdenum": "oil_analysis_results.samples[].spectrographic_analysis_ppm.molybdenum_ppm",
                "titanium": None,
                "manganese": None,
                "antimony": None
            },
            "ContaminantElements": {
                "silicon": "oil_analysis_results.samples[].spectrographic_analysis_ppm.silicon_ppm",
                "sodium": None,
                "potassium": None,
                "boron": None,
                "vanadium": None,
                "lithium": None,
                "cadmium": None
            },
            "AdditiveElements": {
                "calcium": "oil_analysis_results.samples[].spectrographic_analysis_ppm.calcium_ppm",
                "magnesium": None,
                "zinc": "oil_analysis_results.samples[].spectrographic_analysis_ppm.zinc_ppm",
                "phosphorus": "oil_analysis_results.samples[].spectrographic_analysis_ppm.phosphorus_ppm",
                "barium": None
            }
        }
    ], 
    "AnalysisResults": {
        "oilRating": None,
        "unitRating": None,
        "diagnosis": "oil_analysis_results.summary.final_recommendation",
        "recommendations": None,
        "actionRequired": None,
        "nextSampleDue": None,
        "sampleFrequency": None
    },
    "QualityAndCompliance": {
        "reportStatus": "report_header.overall_status",
        "report ": None,
        "frequency": None,
        "dueStatus": None
    }
}


enos_field_map = {
        "testLab": "ENOS",

    "LatestSampleIdentification":{
        "sampleNumber": "oil_analysis_results.samples[-1].sample_information.lab_order_number",
        "bottleNumber": None,
        "analysisNumber": None},

    "EquipmentInformation": {
        "testLabExtracted": "report_header.report_provider_company",
        "vesselNameExtracted": "report_header.equipment_information.vessel_name",
        "imoExtracted": "report_header.equipment_information.imo_number",
        "customerCompany": "report_header.equipment_information.company_name",
        "machineryName": "report_header.equipment_information.machinery_unit",
        "equipmentMake": "report_header.equipment_information.equipment_make",
        "equipmentModel": "report_header.equipment_information.equipment_model",
        "equipmentSerial": None,
        "sampleLocation": "report_header.equipment_information.sample_location",
        "machineryUnit": None,
        "portLanded": None,
        "oilGrade": "oil_analysis_results.samples[3].usage_information.oilgrade_in_use",
        "oilSystemCapacity": None
    },
    "Samples": [
        {
        "sampleNumber": "oil_analysis_results.samples[].sample_information.lab_order_number",
        "sampleDate": "oil_analysis_results.samples[].sample_information.sampling_date",
        "dateReported": "oil_analysis_results.samples[].sample_information.date_reported",
        
            "OilAndOperatingConditions": {
                "oilBrand": None,
                "fuelGrade": "oil_analysis_results.samples[].usage_information.fuel_used",
                "fuelSulfurContent": None,
                "equipmentHours": "oil_analysis_results.samples[].usage_information.equipment_life_h",
                "oilServiceHours": "oil_analysis_results.samples[].usage_information.oil_life_h",
                "oilAddedVolume": "oil_analysis_results.samples[].usage_information.oil_added_l",
                "dailyMakeupVolume": None,
                "consumptionRate": None
            },
            "PhysicalAndChemicalProperties": {
                "appearance": None,
                "color": "oil_analysis_results.samples[].oil_analysis.astm_color",
                "viscosity40c": "oil_analysis_results.samples[].oil_analysis.viscosity_40c_mm2_s",
                "viscosity100c": None,
                "viscosityIndex": None,
                "acidNumber": "oil_analysis_results.samples[].oil_analysis.total_acid_number_mg_koh_g",
                "baseNumber": None,
                "waterContent": "oil_analysis_results.samples[].oil_analysis.water_content_percent_w",
                "freeWater": None,
                "chlorideContent": "oil_analysis_results.samples[].oil_analysis.chloride_nature_of_water",
                "flashPoint": None,
                "oxidationFtir": None,
                "nitrationFtir": None,
                "sootContent": None,
                "pqIndex": None
            },
            "ParticleContamination": {
                "particles4um": None,
                "particles6um": None,
                "particles14um": None,
                "particles21um": None,
                "particles38um": None,
                "particles70um": None,
                "isoCode": None
            },
            "WearElements": {
                "iron": "oil_analysis_results.samples[].element_analysis_ppm.iron_fe_ppm",
                "copper": "oil_analysis_results.samples[].element_analysis_ppm.copper_cu_ppm",
                "lead": "oil_analysis_results.samples[].element_analysis_ppm.lead_pb_ppm",
                "tin": "oil_analysis_results.samples[].element_analysis_ppm.tin_sn_ppm",
                "aluminum": "oil_analysis_results.samples[].element_analysis_ppm.aluminnium_al_ppm",
                "chromium": "oil_analysis_results.samples[].element_analysis_ppm.chromium_cr_ppm",
                "nickel": "oil_analysis_results.samples[].element_analysis_ppm.nickel_ni_ppm",
                "silver": "oil_analysis_results.samples[].element_analysis_ppm.silver_ag_ppm",
                "molybdenum": "oil_analysis_results.samples[].element_analysis_ppm.molybdenum_mo_ppm",
                "titanium": "oil_analysis_results.samples[].element_analysis_ppm.titanium_ti_ppm",
                "manganese": "oil_analysis_results.samples[].element_analysis_ppm.manganese_mn_ppm",
                "antimony": None
            },
            "ContaminantElements": {
                "silicon": "oil_analysis_results.samples[].element_analysis_ppm.silicon_si_ppm",
                "sodium": "oil_analysis_results.samples[].element_analysis_ppm.sodium_na_ppm",
                "potassium": "oil_analysis_results.samples[].element_analysis_ppm.potassium_k_ppm",
                "boron": "oil_analysis_results.samples[].element_analysis_ppm.boron_b_ppm",
                "vanadium": "oil_analysis_results.samples[].element_analysis_ppm.vanadium_v_ppm",
                "lithium": "oil_analysis_results.samples[].element_analysis_ppm.lithium_li_ppm",
                "cadmium": "oil_analysis_results.samples[].element_analysis_ppm.cadmium_cd_ppm"
            },
            "AdditiveElements": {
                "calcium": "oil_analysis_results.samples[].element_analysis_ppm.calcium_ca_ppm",
                "magnesium": "oil_analysis_results.samples[].element_analysis_ppm.magnesium_mg_ppm",
                "zinc": "oil_analysis_results.samples[].element_analysis_ppm.zinc_zn_ppm",
                "phosphorus": "oil_analysis_results.samples[].element_analysis_ppm.phosphorus_p_ppm",
                "barium": "oil_analysis_results.samples[].element_analysis_ppm.barium_ba_ppm"
            }
        }
    ],
    "AnalysisResults": {
        "oilRating": None,
        "unitRating": None,
        "diagnosis": "oil_analysis_results.diagnosis_remarks.remarks",
        "recommendations": None,
        "actionRequired": None,
        "nextSampleDue": None,
        "sampleFrequency": None
    },
    "QualityAndCompliance": {
        "reportStatus": "oil_analysis_results.samples[-1].usage_information.lubricant_condition",
        "report ": None,
        "frequency": None,
        "dueStatus": None
    }
}



gulf_field_map = {
        "testLab": "Gulf",

    "LatestSampleIdentification": {
        "sampleNumber": "oil_analysis_results.samples[-1].sample_information.sample_no",
        "bottleNumber": "oil_analysis_results.samples[-1].sample_information.bottle_no",
        "analysisNumber": None
    },

    "EquipmentInformation": {
        "testLabExtracted": "report_header.report_provider_company",
        "vesselNameExtracted": "report_header.equipment_information.vessel_name",
        "imoExtracted": "report_header.equipment_information.imo_number",
        "customerCompany": "report_header.equipment_information.customer_name",
        "machineryName": "report_header.equipment_information.machinery_unit",
        "equipmentMake": "report_header.equipment_information.equipment_make",
        "equipmentModel": "report_header.equipment_information.equipment_model",
        "equipmentSerial": "report_header.equipment_information.equipment_sn",
        "sampleLocation": "report_header.equipment_information.sample_location",
        "machineryUnit": None,
        "portLanded": "oil_analysis_results.samples[-1].sample_information.port_of_landing",
        "oilGrade": "oil_analysis_results.samples[-1].sample_information.oil_on_label",
        "oilSystemCapacity": None
    },
    "Samples": [
        {
        "sampleNumber": "oil_analysis_results.samples[].sample_information.sample_no",
        "sampleDate": "oil_analysis_results.samples[].sample_information.sampled_date",
        "dateReported": None,

            "OilAndOperatingConditions": {
                "oilBrand": "oil_analysis_results.samples[].sample_information.oil_on_label",
                "fuelGrade": None,
                "fuelSulfurContent": "oil_analysis_results.samples[].sample_information.fuel_in_use_sulphur_percent",
                "equipmentHours": "oil_analysis_results.samples[].sample_information.total_frame_running_hours",
                "oilServiceHours": "oil_analysis_results.samples[].sample_information.lubricant_hours",
                "oilAddedVolume": None,
                "dailyMakeupVolume": None,
                "consumptionRate": None
            },
            "PhysicalAndChemicalProperties": {
                "appearance": None,
                "color": None,
                "viscosity40c": "oil_analysis_results.samples[].analysis.viscosity_cst_mm2_s",
                "viscosity100c": None,
                "viscosityIndex": "oil_analysis_results.samples[].analysis.viscosity_index",
                "acidNumber": "oil_analysis_results.samples[].analysis.an_mgkoh_g",
                "baseNumber": None,
                "waterContent": "oil_analysis_results.samples[].analysis.water_percent_wt",
                "freeWater": None,
                "chlorideContent": None,
                "flashPoint": None,
                "oxidationFtir": None,
                "nitrationFtir": None,
                "sootContent": None,
                "pqIndex": "oil_analysis_results.samples[].analysis.pq_index_2ml"
            },
            "ParticleContamination": {
                "particles4um": "oil_analysis_results.samples[].analysis.greater_than_4_um",
                "particles6um": "oil_analysis_results.samples[].analysis.greater_than_6_um",
                "particles14um": "oil_analysis_results.samples[].analysis.greater_than_14_um",
                "particles21um": None,
                "particles38um": None,
                "particles70um": None,
                "isoCode": "oil_analysis_results.samples[].analysis.iso_code"
            },
            "WearElements": {
                "iron": "oil_analysis_results.samples[].wear_elements_ppm.iron_fe_ppm",
                "copper": "oil_analysis_results.samples[].wear_elements_ppm.copper_cu_ppm",
                "lead": "oil_analysis_results.samples[].wear_elements_ppm.lead_pb_ppm",
                "tin": "oil_analysis_results.samples[].wear_elements_ppm.tin_sn_ppm",
                "aluminum": "oil_analysis_results.samples[].wear_elements_ppm.aluminum_al_ppm",
                "chromium": "oil_analysis_results.samples[].wear_elements_ppm.chromium_cr_ppm",
                "nickel": "oil_analysis_results.samples[].other_elements_ppm.nickel_ni_ppm",
                "silver": "oil_analysis_results.samples[].other_elements_ppm.silver_ag_ppm",
                "molybdenum": "oil_analysis_results.samples[].other_elements_ppm.molybdenum_mo_ppm",
                "titanium": None,
                "manganese": None,
                "antimony": None
            },
            "ContaminantElements": {
                "silicon": "oil_analysis_results.samples[].other_elements_ppm.silicon_si_ppm",
                "sodium": "oil_analysis_results.samples[].other_elements_ppm.sodium_na_ppm",
                "potassium": None,
                "boron": "oil_analysis_results.samples[].other_elements_ppm.boron_b_ppm",
                "vanadium": "oil_analysis_results.samples[].other_elements_ppm.vanadium_v_ppm",
                "lithium": "oil_analysis_results.samples[].other_elements_ppm.lithium_li_ppm",
                "cadmium": None
            },
            "AdditiveElements": {
                "calcium": None,
                "magnesium": None,
                "zinc": None,
                "phosphorus": None,
                "barium": "oil_analysis_results.samples[].other_elements_ppm.barium_ba_ppm"
            }
        }
    ],
    "AnalysisResults": {
        "oilRating": None,
        "unitRating": None,
        "diagnosis": None,
        "recommendations": "oil_analysis_results.recommendations.text",
        "actionRequired": None,
        "nextSampleDue": None,
        "sampleFrequency": None
    },
    "QualityAndCompliance": {
        "reportStatus": "oil_analysis_results.samples[-1].sample_information.lubricant_condition",
        "report ": None,
        "frequency": None,
        "dueStatus": None
    }
}

total_field_map = {
        "testLab": "Total",

    "LatestSampleIdentification": {
        "sampleNumber": "report_header.equipment_information.sample_no",
        "bottleNumber": None,
        "analysisNumber": "report_header.equipment_information.analysis_no"
    },

    "EquipmentInformation": {
        "testLabExtracted": "report_header.report_provider_company",
        "vesselNameExtracted": "report_header.equipment_information.vessel_name",
        "imoExtracted": "report_header.equipment_information.imo", #Lubmarine reports do not contain IMO number
        "customerCompany": "report_header.equipment_information.company",
        "machineryName": "report_header.equipment_information.unit_name",
        "equipmentMake": None,
        "equipmentModel": None,
        "equipmentSerial": None,
        "sampleLocation": "report_header.equipment_information.description",
        "machineryUnit": "report_header.equipment_information.unit_id",
        "portLanded": "oil_analysis_results.samples[-1].sample_data.port_landed",
        "oilGrade": "report_header.equipment_information.oil_type",
        "oilSystemCapacity": None,
    },
    "Samples": [
{
        "sampleNumber": "oil_analysis_results.samples[].sample_data.sample_no",
        "sampleDate": "oil_analysis_results.samples[].sample_data.date_sampled",
        "dateReported": "report_header.equipment_information.reported",

            "OilAndOperatingConditions": {
                "oilBrand": "oil_analysis_results.samples[].sample_data.oil_on_label",
                "fuelGrade": None,
                "fuelSulfurContent": None,
                "equipmentHours": "oil_analysis_results.samples[].sample_data.equipment_life",
                "oilServiceHours": "oil_analysis_results.samples[].sample_data.oil_life",
                "oilAddedVolume": "oil_analysis_results.samples[].sample_data.top_up_volume",
                "dailyMakeupVolume": None,
                "consumptionRate": None
            },
            "PhysicalAndChemicalProperties": {
                "appearance": None,
                "color": None,
                "viscosity40c": "oil_analysis_results.samples[].analysis.visco_40c_mm2s",
                "viscosity100c": None,
                "viscosityIndex": None,
                "acidNumber": "oil_analysis_results.samples[].analysis.acid_number_mg_kohg",
                "baseNumber": None,
                "waterContent": "oil_analysis_results.samples[].analysis.water_content_percent_mass",
                "freeWater": None,
                "chlorideContent": "oil_analysis_results.samples[].analysis.Chlorides",
                "flashPoint": None,
                "oxidationFtir": "oil_analysis_results.samples[].analysis.oxidation_by_ftir_abs_cm",
                "nitrationFtir": None,
                "sootContent": None,
                "pqIndex": "oil_analysis_results.samples[].analysis.pq_index"
            },
            "ParticleContamination": {
                "particles4um": None,
                "particles6um": None,
                "particles14um": None,
                "particles21um": None,
                "particles38um": None,
                "particles70um": None,
                "isoCode": None
            },
            "WearElements": {
                "iron": "oil_analysis_results.samples[].spectro_analysis.wear_elements.iron_fe",
                "copper": "oil_analysis_results.samples[].spectro_analysis.wear_elements.copper_cu",
                "lead": "oil_analysis_results.samples[].spectro_analysis.wear_elements.lead_pb",
                "tin": "oil_analysis_results.samples[].spectro_analysis.wear_elements.tin_sn",
                "aluminum": "oil_analysis_results.samples[].spectro_analysis.wear_elements.aluminum_al",
                "chromium": "oil_analysis_results.samples[].spectro_analysis.wear_elements.chromium_cr",
                "nickel": "oil_analysis_results.samples[].spectro_analysis.contaminants.nickel_ni",
                "silver": "oil_analysis_results.samples[].spectro_analysis.wear_elements.silver_ag",
                "molybdenum": "oil_analysis_results.samples[].spectro_analysis.wear_elements.molybdenum_mo",
                "titanium": None,
                "manganese": None,
                "antimony": None
            },
            "ContaminantElements": {
                "silicon": "oil_analysis_results.samples[].spectro_analysis.contaminants.silicon_si",
                "sodium": "oil_analysis_results.samples[].spectro_analysis.contaminants.sodium_Na",
                "potassium": None,
                "boron": "oil_analysis_results.samples[].spectro_analysis.contaminants.boron_b",
                "vanadium": "oil_analysis_results.samples[].spectro_analysis.contaminants.vanadium_v",
                "lithium": None,
                "cadmium": None
            },
            "AdditiveElements": {
                "calcium": "oil_analysis_results.samples[].spectro_analysis.other_metals.calcium_ca",
                "magnesium": "oil_analysis_results.samples[].spectro_analysis.other_metals.magnesium_mg",
                "zinc": "oil_analysis_results.samples[].spectro_analysis.other_metals.zinc_zn",
                "phosphorus": "oil_analysis_results.samples[].spectro_analysis.other_metals.phosphorus_p",
                "barium": "oil_analysis_results.samples[].spectro_analysis.other_metals.barium_ba"
            }
        }
    ],
    "AnalysisResults": {
        "oilRating": None,
        "unitRating": None,
        "diagnosis": "oil_analysis_results.summary.symptoms",
        "recommendations": "oil_analysis_results.summary.comments",
        "actionRequired": None,
        "nextSampleDue": None,
        "sampleFrequency": None
    },
    "QualityAndCompliance": {
        "reportStatus": "oil_analysis_results.samples[-1].sample_data.status",
        "report ": None,
        "frequency": None,
        "dueStatus": None
    }
}


tribocare_field_map = {
    "testLab": "Tribocare",

  "LatestSampleIdentification": {
    "sampleNumber": "oil_analysis_results.samples[0].sample_details.sample_no",
    "bottleNumber": "oil_analysis_results.samples[0].sample_details.bottle_no",
    "analysisNumber": None
  },

  "EquipmentInformation": {
    "testLabExtracted": "report_header.report_provider_company",
    "vesselNameExtracted": "report_header.vessel_name",
    "imoExtracted": "report_header.vessel_imo",  
    "customerCompany": None,
    "machineryName": "report_header.machinery_name",
    "equipmentMake": "report_header.manufacturer_details.manufacturer",
    "equipmentModel": "report_header.manufacturer_details.model",
    "equipmentSerial": None,
    "sampleLocation": None,
    "machineryUnit": None,
    "portLanded": "report_header.manufacturer_details.port_landed",
    "oilGrade": "oil_analysis_results.samples[0].sample_details.oil_grade_in_use",
    "oilSystemCapacity": "report_header.manufacturer_details.volume_ltr"
  },
  "Samples": [
      {
        "sampleDate": "oil_analysis_results.samples[].sample_details.sampled_date",
        "dateReported": None,
        "sampleNumber": "oil_analysis_results.samples[].sample_details.sample_no",

      "OilAndOperatingConditions": {
        "oilBrand": None,
        "fuelGrade": "report_header.product_information.fuel_grade_or_type", 
        "fuelSulfurContent": None,
        "equipmentHours": "oil_analysis_results.samples[].sample_details.unit_service_hrs",
        "oilServiceHours": "oil_analysis_results.samples[].sample_details.oil_service_hrs",
        "oilAddedVolume": None,
        "dailyMakeupVolume": "oil_analysis_results.samples[].sample_details.daily_makeup_l",
        "consumptionRate": None
      },
      "PhysicalAndChemicalProperties": {
        "appearance": "oil_analysis_results.samples[].analysis.appearance",
        "color": None,
        "viscosity40c": "oil_analysis_results.samples[].analysis.kv_at_40c_mm2s",
        "viscosity100c": None,
        "viscosityIndex": None,
        "acidNumber": "oil_analysis_results.samples[].analysis.an_mgkoh_g",
        "baseNumber": None,
        "waterContent": "oil_analysis_results.samples[].analysis.water_percent_vol",
        "freeWater": None,
        "chlorideContent": "oil_analysis_results.samples[].analysis.chloride_cl_ppm",
        "flashPoint": None,
        "oxidationFtir": "oil_analysis_results.samples[].analysis.oxidation_abs_0_1mm",
        "nitrationFtir": None,
        "sootContent": "oil_analysis_results.samples[].analysis.soot_insol_percent_wt",
        "pqIndex": "oil_analysis_results.samples[].analysis.pq_index_2ml"
      },
      "ParticleContamination": {
        "particles4um": None,
        "particles6um": None,
        "particles14um": None,
        "particles21um": None,
        "particles38um": None,
        "particles70um": None,
        "isoCode": None
      },
      "WearElements": {
        "iron": "oil_analysis_results.samples[].wear_elements_ppm.iron_fe",
        "copper": "oil_analysis_results.samples[].wear_elements_ppm.copper_cu",
        "lead": "oil_analysis_results.samples[].wear_elements_ppm.lead_pb",
        "tin": "oil_analysis_results.samples[].wear_elements_ppm.tin_sn",
        "aluminum": None,
        "chromium": "oil_analysis_results.samples[].wear_elements_ppm.chromium_cr",
        "nickel": "oil_analysis_results.samples[].wear_elements_ppm.nickel_ni",
        "silver": None,
        "molybdenum": None,
        "titanium": None,
        "manganese": None,
        "antimony": "oil_analysis_results.samples[].wear_elements_ppm.antimony_sb"
      },
      "ContaminantElements": {
        "silicon": "oil_analysis_results.samples[].contaminant_elements_ppm.silicon_si",
        "sodium": "oil_analysis_results.samples[].contaminant_elements_ppm.sodium_na",
        "potassium": None,
        "boron": "oil_analysis_results.samples[].contaminant_elements_ppm.boron_b",
        "vanadium": None,
        "lithium": None,
        "cadmium": None
      },
      "AdditiveElements": {
        "calcium": "oil_analysis_results.samples[].additive_elements_ppm.calcium_ca",
        "magnesium": "oil_analysis_results.samples[].additive_elements_ppm.magnesium_mg",
        "zinc": "oil_analysis_results.samples[].additive_elements_ppm.zinc_zn",
        "phosphorus": "oil_analysis_results.samples[].additive_elements_ppm.phosphorus_p",
        "barium": None
      }
    }
  ],
  "AnalysisResults": {
    "oilRating": "report_header.report_summary.oil_rating_comment",
    "unitRating": "report_header.report_summary.unit_rating_comment",
    "diagnosis": None,
    "recommendations": "report_header.report_summary.action_required",
    "actionRequired": None,
    "nextSampleDue": None,
    "sampleFrequency": None
  },
  "QualityAndCompliance": {
    "reportStatus": "oil_analysis_results.samples[0].sample_details.rating",
    "report ": None,
    "frequency": None,
    "dueStatus": None
    }
}

viswa_field_map = {
    "testLab": "Viswa",

    "LatestSampleIdentification": {
        "sampleNumber": "oil_analysis_results.samples[0].general_details.report_id",
        "bottleNumber": "oil_analysis_results.samples[0].general_details.bottle_identification_no",
        "analysisNumber": None
    },
        
    "EquipmentInformation": {
        "testLabExtracted": "report_header.report_provider_company",
        "vesselNameExtracted": "report_header.customer_details.vessel",
        "imoExtracted": "report_header.customer_details.imo_no",
        "customerCompany": "report_header.customer_details.customer",
        "machineryName": "report_header.customer_details.equipment",
        "equipmentMake": None,
        "equipmentModel": None,
        "equipmentSerial": None,
        "sampleLocation": "oil_analysis_results.samples[0].general_details.sampling_point",
        "machineryUnit": None,
        "portLanded": "oil_analysis_results.samples[0].general_details.place",
        "oilGrade": "report_header.customer_details.brand_and_grade",
        "oilSystemCapacity": None
    },
    "Samples": [
        {
        "sampleNumber": "oil_analysis_results.samples[].general_details.report_id",
        "sampleDate": "oil_analysis_results.samples[].general_details.sampling_date",
        "dateReported": "oil_analysis_results.samples[].general_details.report_date",

            "OilAndOperatingConditions": {
                "oilBrand": None,
                "fuelGrade": None,
                "fuelSulfurContent": None,
                "equipmentHours": "oil_analysis_results.samples[].general_details.unit_usage",
                "oilServiceHours": "oil_analysis_results.samples[].general_details.total_lubricant_hours",
                "oilAddedVolume": "oil_analysis_results.samples[].general_details.oil_added_ltrs",
                "dailyMakeupVolume": None,
                "consumptionRate": None
            },
            "PhysicalAndChemicalProperties": {
                "appearance": None,
                "color": None,
                "viscosity40c": "oil_analysis_results.samples[].chemistry.vis_40c_cst",
                "viscosity100c": None,
                "viscosityIndex": None,
                "acidNumber": "oil_analysis_results.samples[].chemistry.total_acid_mg_kohg",
                "baseNumber": None,
                "waterContent": "oil_analysis_results.samples[].contamination.water_percent",
                "freeWater": None,
                "chlorideContent": None,
                "flashPoint": None,
                "oxidationFtir": "oil_analysis_results.samples[].chemistry.ir_oxidation_au",
                "nitrationFtir": "oil_analysis_results.samples[].contamination.ir_nitration_au",
                "sootContent": None,
                "pqIndex": None
            },
            "ParticleContamination": {
                "particles4um": "oil_analysis_results.samples[].particle_count.gt_4u",
                "particles6um": "oil_analysis_results.samples[].particle_count.gt_6u",
                "particles14um": "oil_analysis_results.samples[].particle_count.gt_14u",
                "particles21um": None,
                "particles38um": None,
                "particles70um": None,
                "isoCode": "oil_analysis_results.samples[].particle_count.iso_code"
            },
            "WearElements": {
                "iron": "oil_analysis_results.samples[].wear_ppm.iron_ppm",
                "copper": "oil_analysis_results.samples[].wear_ppm.copper_ppm",
                "lead": "oil_analysis_results.samples[].wear_ppm.lead_ppm",
                "tin": "oil_analysis_results.samples[].wear_ppm.tin_ppm",
                "aluminum": "oil_analysis_results.samples[].wear_ppm.aluminium_ppm",
                "chromium": "oil_analysis_results.samples[].wear_ppm.chromium_ppm",
                "nickel": "oil_analysis_results.samples[].wear_ppm.nickel_ppm",
                "silver": "oil_analysis_results.samples[].wear_ppm.silver_ppm",
                "molybdenum": "oil_analysis_results.samples[].wear_ppm.molybdenum_ppm",
                "titanium": "oil_analysis_results.samples[].wear_ppm.titanium_ppm",
                "manganese": "oil_analysis_results.samples[].chemistry.manganese_ppm",
                "antimony": "oil_analysis_results.samples[].wear_ppm.antimony_ppm"
            },
            "ContaminantElements": {
                "silicon": "oil_analysis_results.samples[].contamination.silicon_ppm",
                "sodium": "oil_analysis_results.samples[].contamination.sodium_ppm",
                "potassium": "oil_analysis_results.samples[].chemistry.potassium_ppm",
                "boron": "oil_analysis_results.samples[].contamination.boron_ppm",
                "vanadium": "oil_analysis_results.samples[].contamination.vanadium_ppm",
                "lithium": None,
                "cadmium": None
            },
            "AdditiveElements": {
                "calcium": "oil_analysis_results.samples[].chemistry.calcium_ppm",
                "magnesium": "oil_analysis_results.samples[].chemistry.magnesium_ppm",
                "zinc": "oil_analysis_results.samples[].chemistry.zinc_ppm",
                "phosphorus": "oil_analysis_results.samples[].chemistry.phosphorus_ppm",
                "barium": "oil_analysis_results.samples[].chemistry.barium_ppm"
            }
        }
    ],
    "AnalysisResults": {
        "oilRating": None,
        "unitRating": None,
        "diagnosis": "report_header.comments",
        "recommendations": None,
        "actionRequired": None,
        "nextSampleDue": None,
        "sampleFrequency": None
    },
    "QualityAndCompliance": {
        "reportStatus": "oil_analysis_results.samples[0].general_details.oil_condition_rating",
        "report ": None,
        "frequency": None,
        "dueStatus": None
    }
}

vps_field_map = {
        "testLab": "VPS",

    "LatestSampleIdentification": {
        "sampleNumber": "oil_analysis_results.samples[0].test_results.sample_number",
        "bottleNumber": None,
        "analysisNumber": None
    },

    "EquipmentInformation": {
        "testLabExtracted": "report_header.report_provider_company",
        "vesselNameExtracted": "report_header.vessel_name",
        "imoExtracted": "report_header.vessel_imo",
        "customerCompany": None,
        "machineryName": "report_header.part_name",
        "equipmentMake": "report_header.sample_details.manufacturer",
        "equipmentModel": "report_header.sample_details.model",
        "equipmentSerial": None,
        "sampleLocation": "oil_analysis_results.samples[0].test_results.sampling_point",
        "machineryUnit": None,
        "portLanded": None,
        "oilGrade": "oil_analysis_results.samples[0].test_results.lube_grade",
        "oilSystemCapacity": "report_header.sample_details.oil_quantity_in_system_litres",
    },
    "Samples": [
{
        "sampleNumber": "oil_analysis_results.samples[].test_results.sample_number",
        "bottleNumber": None,
        "sampleDate": "oil_analysis_results.samples[].test_results.sampling_date",
 
            "OilAndOperatingConditions": {
                "oilBrand": "report_header.sample_details.oil_brand",
                "fuelGrade": "oil_analysis_results.samples[].test_results.fuel_in_use",
                "fuelSulfurContent": None,
                "equipmentHours": "oil_analysis_results.samples[].test_results.unit_service_hrs",
                "oilServiceHours": "oil_analysis_results.samples[].test_results.oil_service_hrs",
                "oilAddedVolume": None,
                "dailyMakeupVolume": "oil_analysis_results.samples[].test_results.oil_top_up_volume_daily",
                "consumptionRate": None
            },
            "PhysicalAndChemicalProperties": {
                "appearance": None,
                "color": None,
                "viscosity40c": "oil_analysis_results.samples[].lubricant_data.viscosity_at_40c",
                "viscosity100c": "oil_analysis_results.samples[].lubricant_data.viscosity_at_100c",
                "viscosityIndex": "oil_analysis_results.samples[].lubricant_data.viscosity_index",
                "acidNumber": "oil_analysis_results.samples[].lubricant_data.acid_number",
                "baseNumber": None,
                "waterContent": "oil_analysis_results.samples[].contaminants.water",
                "freeWater": None,
                "chlorideContent": None,
                "flashPoint": None,
                "oxidationFtir": "oil_analysis_results.samples[].lubricant_data.oxidation",
                "nitrationFtir": None,
                "sootContent": None,
                "pqIndex": None
            },
            "ParticleContamination": {
                "particles4um": "oil_analysis_results.samples[].contaminants.particle_count_4_micron_c",
                "particles6um": "oil_analysis_results.samples[].contaminants.particle_count_6_micron_c",
                "particles14um": "oil_analysis_results.samples[].contaminants.particle_count_14_micron_c",
                "particles21um": None,
                "particles38um": None,
                "particles70um": None,
                "isoCode": "oil_analysis_results.samples[].contaminants.iso_4406_code_number"
            },
            "WearElements": {
                "iron": "oil_analysis_results.samples[].wear.iron",
                "copper": "oil_analysis_results.samples[].wear.copper",
                "lead": "oil_analysis_results.samples[].wear.lead",
                "tin": "oil_analysis_results.samples[].wear.tin",
                "aluminum": "oil_analysis_results.samples[].wear.aluminium",
                "chromium": "oil_analysis_results.samples[].wear.chromium",
                "nickel": "oil_analysis_results.samples[].contaminants.nickel",
                "silver": "oil_analysis_results.samples[].wear.silver",
                "molybdenum": "oil_analysis_results.samples[].wear.molybdenum",
                "titanium": "oil_analysis_results.samples[].wear.titanium",
                "manganese": "oil_analysis_results.samples[].wear.manganese",
                "antimony": "oil_analysis_results.samples[].additives_ppm.antimony"
            },
            "ContaminantElements": {
                "silicon": "oil_analysis_results.samples[].contaminants.silicon",
                "sodium": "oil_analysis_results.samples[].contaminants.sodium",
                "potassium": "oil_analysis_results.samples[].contaminants.potassium",
                "boron": "oil_analysis_results.samples[].additives_ppm.boron",
                "vanadium": "oil_analysis_results.samples[].contaminants.vanadium",
                "lithium": "oil_analysis_results.samples[].additives_ppm.lithium",
                "cadmium": "oil_analysis_results.samples[].additives_ppm.cadmium"
            },
            "AdditiveElements": {
                "calcium": "oil_analysis_results.samples[].additives_ppm.calcium",
                "magnesium": "oil_analysis_results.samples[].additives_ppm.magnesium",
                "zinc": "oil_analysis_results.samples[].additives_ppm.zinc",
                "phosphorus": "oil_analysis_results.samples[].additives_ppm.phosphorus",
                "barium": "oil_analysis_results.samples[].additives_ppm.barium"
            }
        }
    ],
    "AnalysisResults": {
        "oilRating": None,
        "unitRating": None,
        "diagnosis": "oil_analysis_results.oil_comment",
        "recommendations": "oil_analysis_results.unit_comment",
        "actionRequired": "oil_analysis_results.note",
        "nextSampleDue": None,
        "sampleFrequency": None
    },
    "QualityAndCompliance": {
        "reportStatus": "oil_analysis_results.samples[0].test_results.rating",
        "report ": None,
        "frequency": None,
        "dueStatus": None
    }
}

nof_field_map = {
        "testLab": "NOF",

    "LatestSampleIdentification": {
        "sampleNumber": "oil_analysis_results.samples[-1].sample_details.sample_number",
        "bottleNumber": None,
        "analysisNumber": None
    },

    "EquipmentInformation": {
        "testLabExtracted": "report_header.report_provider_details.report_provider_company",
        "vesselNameExtracted": "report_header.asset_details.vessel",
        "imoExtracted": "report_header.asset_details.imo_number",
        "customerCompany": None,
        "machineryName": "oil_analysis_results.samples[-1].sample_details.machinery",
        "equipmentMake": None,
        "equipmentModel": None,
        "equipmentSerial": None,
        "sampleLocation": None,
        "machineryUnit": None,
        "portLanded": None,
        "oilGrade": "oil_analysis_results.samples[-1].sample_details.product",
        "oilSystemCapacity": None
    },
    "Samples": [
        {
        "sampleNumber": "oil_analysis_results.samples[].sample_details.sample_number",
        "sampleDate": "oil_analysis_results.samples[].sample_details.date_sampled",
        "dateReported": None,

            "OilAndOperatingConditions": {
                "oilBrand": None,
                "fuelGrade": None,
                "fuelSulfurContent": None,
                "equipmentHours": None,
                "oilServiceHours": "oil_analysis_results.samples[].sample_details.running_time_since_last_oil_change_hrs",
                "oilAddedVolume": None,
                "dailyMakeupVolume": None,
                "consumptionRate": None
            },
            "PhysicalAndChemicalProperties": {
                "appearance": None,
                "color": None,
                "viscosity40c": "oil_analysis_results.samples[].oil_properties.kv_at_40c_mm2s",
                "viscosity100c": None,
                "viscosityIndex": None,
                "acidNumber": "oil_analysis_results.samples[].oil_properties.acid_number_mg_koh_g",
                "baseNumber": None,
                "waterContent": "oil_analysis_results.samples[].oil_properties.water_mass_percent",
                "freeWater": None,
                "chlorideContent": None,
                "flashPoint": None,
                "oxidationFtir": None,
                "nitrationFtir": None,
                "sootContent": None,
                "pqIndex": None
            },
            "ParticleContamination": {
                "particles4um": None,
                "particles6um": None,
                "particles14um": None,
                "particles21um": None,
                "particles38um": None,
                "particles70um": None,
                "isoCode": None
            },
            "WearElements": {
                "iron": "oil_analysis_results.samples[].elements_mass_ppm.iron_fe",
                "copper": "oil_analysis_results.samples[].elements_mass_ppm.copper_cu",
                "lead": "oil_analysis_results.samples[].elements_mass_ppm.lead_pb",
                "tin": "oil_analysis_results.samples[].elements_mass_ppm.tin_sn",
                "aluminum": "oil_analysis_results.samples[].elements_mass_ppm.aluminium_al",
                "chromium": "oil_analysis_results.samples[].elements_mass_ppm.chromium_cr",
                "nickel": "oil_analysis_results.samples[].elements_mass_ppm.nickel_ni",
                "silver": "oil_analysis_results.samples[].elements_mass_ppm.silver_ag",
                "molybdenum": "oil_analysis_results.samples[].elements_mass_ppm.molybdenum_mo",
                "titanium": None,
                "manganese": None,
                "antimony": None
            },
            "ContaminantElements": {
                "silicon": "oil_analysis_results.samples[].elements_mass_ppm.silicon_si",
                "sodium": "oil_analysis_results.samples[].elements_mass_ppm.sodium_na",
                "potassium": None,
                "boron": "oil_analysis_results.samples[].elements_mass_ppm.boron_b",
                "vanadium": None,
                "lithium": None,
                "cadmium": None
            },
            "AdditiveElements": {
                "calcium": "oil_analysis_results.samples[].elements_mass_ppm.calcium_ca",
                "magnesium": "oil_analysis_results.samples[].elements_mass_ppm.magnesium_mg",
                "zinc": "oil_analysis_results.samples[].elements_mass_ppm.zinc_zn",
                "phosphorus": "oil_analysis_results.samples[].elements_mass_ppm.phosphorus_p",
                "barium": "oil_analysis_results.samples[].elements_mass_ppm.barium_ba"
            }
        }
    ],
    "AnalysisResults": {
        "oilRating": None,
        "unitRating": None,
        "diagnosis": "report_header.comment",
        "recommendations": None,
        "actionRequired": None,
        "nextSampleDue": None,
        "sampleFrequency": None
    },
    "QualityAndCompliance": {
        "reportStatus": "report_header.overall_condition",
        "report ": None,
        "frequency": None,
        "dueStatus": None
    }
}

mobilserv_field_map = {
        "testLab": "Mobil Serv",

    "LatestSampleIdentification": {
        "sampleNumber": "report_header.sample_information.sample_id",
        "bottleNumber": "report_header.sample_information.bottle_id",
        "analysisNumber": None
    },

    "EquipmentInformation": {
        "testLabExtracted": "report_header.report_provider_company",
        "vesselNameExtracted": "report_header.account_information.name",
        "imoExtracted": "report_header.account_information.imo_reg_number",
        "customerCompany": "report_header.account_information.parent_account",
        "machineryName": "report_header.description",
        "equipmentMake": "report_header.equipment_information.manufacturer",
        "equipmentModel": "report_header.equipment_information.model",
        "equipmentSerial": None,
        "sampleLocation": None,
        "machineryUnit": None,
        "portLanded": "oil_analysis_results.samples[-1].sample_info.port_landed",
        "oilGrade": "report_header.sample_information.tested_lubricant",
    },
    "Samples": [
        {
        "sampleNumber": "oil_analysis_results.samples[].sample_id",
        "sampleDate": "oil_analysis_results.samples[].sample_info.sampled_date",
        "dateReported": "oil_analysis_results.samples[].sample_info.reported_date",
        
            "OilAndOperatingConditions": {
                "oilBrand": None,
                "fuelGrade": None,
                "fuelSulfurContent": None,
                "equipmentHours": "oil_analysis_results.samples[].sample_info.total_equipment_hours",
                "oilServiceHours": "oil_analysis_results.samples[].sample_info.oil_service_hours",
                "oilAddedVolume": None,
                "dailyMakeupVolume": "oil_analysis_results.samples[].sample_info.oil_used_in_last_24_hrs",
                "oilSystemCapacity": "oil_analysis_results.samples[].sample_info.used_oil_volume",
                "consumptionRate": None
            },
            "PhysicalAndChemicalProperties": {
                "appearance": None,
                "color": None,
                "viscosity40c": None,
                "viscosity100c": "oil_analysis_results.samples[].lubricant_properties.visc_at_100c_cst",
                "viscosityIndex": None,
                "acidNumber": None,
                "baseNumber": "oil_analysis_results.samples[].lubricant_properties.tbn_mg_koh_g",
                "waterContent": "oil_analysis_results.samples[].lubricant_properties.water_vol_percent",
                "freeWater": None,
                "chlorideContent": None,
                "flashPoint": None,
                "oxidationFtir": "oil_analysis_results.samples[].lubricant_properties.oxidation_ab_cm",
                "nitrationFtir": None,
                "sootContent": "oil_analysis_results.samples[].lubricant_properties.soot_wt_percent",
                "pqIndex": None
            },
            "ParticleContamination": {
                "particles4um": None,
                "particles6um": None,
                "particles14um": None,
                "particles21um": None,
                "particles38um": None,
                "particles70um": None,
                "isoCode": None
            },
            "WearElements": {
                "iron": "oil_analysis_results.samples[].wear_ppm.fe_iron",
                "copper": "oil_analysis_results.samples[].wear_ppm.cu_copper",
                "lead": "oil_analysis_results.samples[].wear_ppm.pb_lead",
                "tin": "oil_analysis_results.samples[].wear_ppm.sn_tin",
                "aluminum": "oil_analysis_results.samples[].wear_ppm.al_aluminium",
                "chromium": "oil_analysis_results.samples[].wear_ppm.cr_chromium",
                "nickel": "oil_analysis_results.samples[].wear_ppm.ni_nickel",
                "silver": "oil_analysis_results.samples[].wear_ppm.ag_silver",
                "molybdenum": "oil_analysis_results.samples[].wear_ppm.mo_molybdenum",
                "titanium": None,
                "manganese": None,
                "antimony": None
            },
            "ContaminantElements": {
                "silicon": "oil_analysis_results.samples[].contaminants_ppm.si_silicon",
                "sodium": "oil_analysis_results.samples[].contaminants_ppm.na_sodium",
                "potassium": "oil_analysis_results.samples[].contaminants_ppm.k_potassium",
                "boron": "oil_analysis_results.samples[].additive_ppm.b_boron",
                "vanadium": "oil_analysis_results.samples[].contaminants_ppm.v_vanadium",
                "lithium": None,
                "cadmium": None
            },
            "AdditiveElements": {
                "calcium": "oil_analysis_results.samples[].additive_ppm.ca_calcium",
                "magnesium": "oil_analysis_results.samples[].additive_ppm.mg_magnesium",
                "zinc": "oil_analysis_results.samples[].additive_ppm.zn_zinc",
                "phosphorus": "oil_analysis_results.samples[].additive_ppm.p_phosphorus",
                "barium": "oil_analysis_results.samples[].additive_ppm.ba_barium"
            }
        }
    ],
    "AnalysisResults": {
        "oilRating": "oil_analysis_results.samples[-1].lubricant_properties.lubricant_rating",
        "unitRating": "oil_analysis_results.samples[-1].lubricant_properties.equipment_rating",
        "diagnosis": None,
        "recommendations": "report_header.recommendation_comments",
        "actionRequired": None,
        "nextSampleDue": None,
        "sampleFrequency": None
    },
    "QualityAndCompliance": {
        "reportStatus": "report_header.report_status",
        "report ": None,
        "frequency": None,
        "dueStatus": None
    }
}

shell_field_map = {
        "testLab": "Shell",

    "LatestSampleIdentification": {
        "sampleNumber": "oil_analysis_results.samples[0].sample_details.sample_number",
        "bottleNumber": None,
        "analysisNumber": None
    },

    "EquipmentInformation": {
        "testLabExtracted": "report_header.report_provider_company",
        "vesselNameExtracted": "report_header.vessel_name",
        "imoExtracted": "report_header.imo_number",
        "customerCompany": "report_header.customer",
        "machineryName": "report_header.equipment_component",
        "equipmentMake": "report_header.manufacturer",
        "equipmentModel": "report_header.model",
        "equipmentSerial": None,
        "sampleLocation": None,
        "machineryUnit": None,
        "portLanded": None,
        "oilGrade": "report_header.registered_lubricant",
    },
    "Samples": [
        {
        "sampleNumber": "oil_analysis_results.samples[].sample_details.sample_number",
        "sampleDate": "oil_analysis_results.samples[].sample_details.sample_date",
        "dateReported": None,
        
            "OilAndOperatingConditions": {
                "oilBrand": None,
                "fuelGrade": "oil_analysis_results.samples[].usage_information.fuel_used",
                "fuelSulfurContent": None,
                "equipmentHours": "oil_analysis_results.samples[].usage_information.equipment_life_hours",
                "oilServiceHours": "oil_analysis_results.samples[].usage_information.lubricant_life_hours",
                "oilAddedVolume": "oil_analysis_results.samples[].usage_information.top_up_volume_litres",
                "dailyMakeupVolume": None,
                "oilSystemCapacity": None,
                "consumptionRate": None
            },
            "PhysicalAndChemicalProperties": {
                "appearance": None,
                "color": None,
                "viscosity40c": None,
                "viscosity100c": "oil_analysis_results.samples[].physical_characteristics.viscosity_100c_cst",
                "viscosityIndex": None,
                "acidNumber": None,
                "baseNumber": "oil_analysis_results.samples[].physical_characteristics.tbn_d2896_mg_koh_g",
                "waterContent": "oil_analysis_results.samples[].contamination_analysis.water_content_percent",
                "freeWater": None,
                "chlorideContent": None,
                "flashPoint": "oil_analysis_results.samples[].physical_characteristics.flash_point_setaflash_c",
                "oxidationFtir": None,
                "nitrationFtir": None,
                "sootContent": None,
                "pqIndex": "oil_analysis_results.samples[].wear_analysis.wpi_index"
            },
            "ParticleContamination": {
                "particles4um": None,
                "particles6um": None,
                "particles14um": None,
                "particles21um": None,
                "particles38um": None,
                "particles70um": None,
                "isoCode": None
            },
            "WearElements": {
                "iron": "oil_analysis_results.samples[].wear_analysis.iron_fe_ppm",
                "copper": "oil_analysis_results.samples[].wear_analysis.copper_cu_ppm",
                "lead": "oil_analysis_results.samples[].wear_analysis.lead_pb_ppm",
                "tin": "oil_analysis_results.samples[].wear_analysis.tin_sn_ppm",
                "aluminum": "oil_analysis_results.samples[].wear_analysis.aluminium_al_ppm",
                "chromium": "oil_analysis_results.samples[].wear_analysis.chromium_cr_ppm",
                "nickel": None,
                "silver": None,
                "molybdenum": "oil_analysis_results.samples[].additive_analysis.molybdenum_mo_ppm",
                "titanium": None,
                "manganese": None,
                "antimony": None
            },
            "ContaminantElements": {
                "silicon": "oil_analysis_results.samples[].contamination_analysis.silicon_si_ppm",
                "sodium": "oil_analysis_results.samples[].contamination_analysis.sodium_na_ppm",
                "potassium": None,
                "boron": "oil_analysis_results.samples[].additive_analysis.boron_b_ppm",
                "vanadium": "oil_analysis_results.samples[].wear_analysis.vanadium_v_ppm",
                "lithium": None,
                "cadmium": None
            },
            "AdditiveElements": {
                "calcium": "oil_analysis_results.samples[].additive_analysis.calcium_ca_percent",
                "magnesium": "oil_analysis_results.samples[].additive_analysis.magnesium_mg_ppm",
                "zinc": "oil_analysis_results.samples[].additive_analysis.zinc_zn_percent",
                "phosphorus": "oil_analysis_results.samples[].additive_analysis.phosphorus_p_percent",
                "barium": "oil_analysis_results.samples[].additive_analysis.barium_ba_percent"
            }
        }
    ],
    "AnalysisResults": {
        "oilRating": "report_header.diagnosis.status",
        "unitRating": None,
        "diagnosis": "report_header.diagnosis.remarks",
        "recommendations": None,
        "actionRequired": None,
        "nextSampleDue": None,
        "sampleFrequency": None
    },
    "QualityAndCompliance": {
        "reportStatus": None,
        "report ": None,
        "frequency": None,
        "dueStatus": None
    }
}


maritec_field_map = {
        "testLab": "Maritec",

    "LatestSampleIdentification": {
        "sampleNumber": "oil_analysis_results.samples[-1].sample_metadata.report_number",
        "bottleNumber": None,
        "analysisNumber": None
    },

    "EquipmentInformation": {
        "testLabExtracted": "report_header.report_provider",
        "vesselNameExtracted": "report_header.vessel_name",
        "imoExtracted": "report_header.vessel_imo",
        "customerCompany": "report_header.recipient_company",
        "machineryName": "report_header.component",
        "equipmentMake": None,
        "equipmentModel": None,
        "equipmentSerial": None,
        "sampleLocation": "oil_analysis_results.samples[-1].sample_metadata.sampling_location",
        "machineryUnit": None,
        "portLanded": "oil_analysis_results.samples[-1].sample_metadata.sent_from",
        "oilGrade": "oil_analysis_results.samples[-1].sample_metadata.oil_brand_grade",
    },
    "Samples": [
        {
        "sampleNumber": "oil_analysis_results.samples[].sample_metadata.report_number",
        "sampleDate": "oil_analysis_results.samples[].sample_metadata.sampling_date",
        "dateReported": "oil_analysis_results.samples[].sample_metadata.report_date",
        
            "OilAndOperatingConditions": {
                "oilBrand": None,
                "fuelGrade": None,
                "fuelSulfurContent": None,
                "equipmentHours": "oil_analysis_results.samples[].sample_metadata.equipment_hours",
                "oilServiceHours": "oil_analysis_results.samples[].sample_metadata.oil_service_hours",
                "oilAddedVolume": None,
                "dailyMakeupVolume": None,
                "oilSystemCapacity":  "oil_analysis_results.samples[].sample_metadata.oil_volume_litres",
                "consumptionRate": None
            },
            "PhysicalAndChemicalProperties": {
                "appearance": None,
                "color": None,
                "viscosity40c": "oil_analysis_results.samples[].lube_oil_properties.kv40_cst",
                "viscosity100c": "oil_analysis_results.samples[].lube_oil_properties.kv100_cst",
                "viscosityIndex": "oil_analysis_results.samples[].lube_oil_properties.viscosity_index",
                "acidNumber": "oil_analysis_results.samples[].lube_oil_properties.acid_number_mgkoh_g",
                "baseNumber": "oil_analysis_results.samples[].lube_oil_properties.base_number_mgkoh_g",
                "waterContent": "oil_analysis_results.samples[].lube_oil_properties.water_content_percent_w",
                "freeWater": None,
                "chlorideContent": None,
                "flashPoint": "oil_analysis_results.samples[].lube_oil_properties.flash_point_pmcc_deg_c",
                "oxidationFtir": None,
                "nitrationFtir": None,
                "sootContent": None,
                "pqIndex": None
            },
            "ParticleContamination": {
                "particles4um": None,
                "particles6um": None,
                "particles14um": None,
                "particles21um": None,
                "particles38um": None,
                "particles70um": None,
                "isoCode": None
            },
            "WearElements": {
                "iron": "oil_analysis_results.samples[].spectrometric_analysis_mg_kg.iron",
                "copper": "oil_analysis_results.samples[].spectrometric_analysis_mg_kg.copper",
                "lead": "oil_analysis_results.samples[].spectrometric_analysis_mg_kg.lead",
                "tin": "oil_analysis_results.samples[].spectrometric_analysis_mg_kg.tin",
                "aluminum": "oil_analysis_results.samples[].spectrometric_analysis_mg_kg.aluminium",
                "chromium": "oil_analysis_results.samples[].spectrometric_analysis_mg_kg.chromium",
                "nickel": "oil_analysis_results.samples[].spectrometric_analysis_mg_kg.nickel",
                "silver": "oil_analysis_results.samples[].spectrometric_analysis_mg_kg.silver",
                "molybdenum": "oil_analysis_results.samples[].spectrometric_analysis_mg_kg.molybdenum",
                "titanium": None,
                "manganese": None,
                "antimony": None
            },
            "ContaminantElements": {
                "silicon": "oil_analysis_results.samples[].spectrometric_analysis_mg_kg.silicon",
                "sodium": "oil_analysis_results.samples[].spectrometric_analysis_mg_kg.sodium",
                "potassium": None,
                "boron": "oil_analysis_results.samples[].spectrometric_analysis_mg_kg.boron",
                "vanadium": "oil_analysis_results.samples[].spectrometric_analysis_mg_kg.vanadium",
                "lithium": None,
                "cadmium": None
            },
            "AdditiveElements": {
                "calcium": "oil_analysis_results.samples[].spectrometric_analysis_mg_kg.calcium",
                "magnesium": "oil_analysis_results.samples[].spectrometric_analysis_mg_kg.magnesium",
                "zinc": "oil_analysis_results.samples[].spectrometric_analysis_mg_kg.zinc",
                "phosphorus": "oil_analysis_results.samples[].spectrometric_analysis_mg_kg.phosphorus",
                "barium": "oil_analysis_results.samples[].spectrometric_analysis_mg_kg.barium"
            }
        }
    ],
    "AnalysisResults": {
        "oilRating": "oil_analysis_results.samples[-1].sample_metadata.status",
        "unitRating": None,
        "diagnosis": "oil_analysis_results.remarks.comment",
        "recommendations": None,
        "actionRequired": None,
        "nextSampleDue": None,
        "sampleFrequency": None
    },
    "QualityAndCompliance": {
        "reportStatus": None,
        "report ": None,
        "frequency": None,
        "dueStatus": None
    }
}

marlab_field_map = {
        "testLab": "Marlab",

    "LatestSampleIdentification": {
        "sampleNumber": "oil_analysis_results.samples[-1].sample_information.lab_order_number",
        "bottleNumber": None,
        "analysisNumber": None
    },

    "EquipmentInformation": {
        "testLabExtracted": "report_header.report_provider_company",
        "vesselNameExtracted": "report_header.equipment_information.vessel_name",
        "imoExtracted": "report_header.equipment_information.imo_number",
        "customerCompany": "report_header.equipment_information.company_name",
        "machineryName": "report_header.equipment_information.machinery_unit",
        "equipmentMake": "report_header.equipment_information.equipment_make",
        "equipmentModel": "report_header.equipment_information.equipment_model",
        "equipmentSerial": None,
        "sampleLocation": None,
        "machineryUnit": None,
        "portLanded": None,
        "oilGrade": "report_header.equipment_information.product_name",
    },
    "Samples": [
        {
        "sampleNumber": "oil_analysis_results.samples[].sample_information.lab_order_number",
        "sampleDate": "oil_analysis_results.samples[].sample_information.sampling_date",
        "dateReported": "oil_analysis_results.samples[].sample_information.date_reported",
        
            "OilAndOperatingConditions": {
                "oilBrand": None,
                "fuelGrade": None,
                "fuelSulfurContent": None,
                "equipmentHours": "oil_analysis_results.samples[].usage_information.equipment_life_hours",
                "oilServiceHours": "oil_analysis_results.samples[].usage_information.oil_life_hours",
                "oilAddedVolume": "oil_analysis_results.samples[].usage_information.oil_added_l",
                "dailyMakeupVolume": None,
                "oilSystemCapacity": None,
                "consumptionRate": None
            },
            "PhysicalAndChemicalProperties": {
                "appearance": None,
                "color": None,
                "viscosity40c": None,
                "viscosity100c": "oil_analysis_results.samples[].physical_properties.viscosity_40c_mm2_s",
                "viscosityIndex": None,
                "acidNumber": "oil_analysis_results.samples[].physical_properties.total_acid_number_mg_koh_g",
                "baseNumber": None,
                "waterContent": "oil_analysis_results.samples[].physical_properties.water_content_ppm",
                "freeWater": None,
                "chlorideContent": None,
                "flashPoint": None,
                "oxidationFtir": None,
                "nitrationFtir": None,
                "sootContent": None,
                "pqIndex": "oil_analysis_results.samples[].physical_properties.pq_index_wpi"
            },
            "ParticleContamination": {
                "particles4um": None,
                "particles6um": None,
                "particles14um": None,
                "particles21um": None,
                "particles38um": None,
                "particles70um": None,
                "isoCode": None
            },
            "WearElements": {
                "iron": "oil_analysis_results.samples[].element_analysis_ppm.iron_ppm",
                "copper": "oil_analysis_results.samples[].element_analysis_ppm.copper_ppm",
                "lead": "oil_analysis_results.samples[].element_analysis_ppm.lead_ppm",
                "tin": "oil_analysis_results.samples[].element_analysis_ppm.tin_ppm",
                "aluminum": "oil_analysis_results.samples[].element_analysis_ppm.aluminium_ppm",
                "chromium": "oil_analysis_results.samples[].element_analysis_ppm.chromium_ppm",
                "nickel": "oil_analysis_results.samples[].element_analysis_ppm.nickel_ppm",
                "silver": "oil_analysis_results.samples[].element_analysis_ppm.silver_ppm",
                "molybdenum": "oil_analysis_results.samples[].element_analysis_ppm.molybdenum_ppm",
                "titanium": None,
                "manganese": None,
                "antimony": None
            },
            "ContaminantElements": {
                "silicon": "oil_analysis_results.samples[].element_analysis_ppm.silicon_ppm",
                "sodium": "oil_analysis_results.samples[].element_analysis_ppm.sodium_ppm",
                "potassium": None,
                "boron": "oil_analysis_results.samples[].element_analysis_ppm.boron_ppm",
                "vanadium": "oil_analysis_results.samples[].element_analysis_ppm.vanadium_ppm",
                "lithium": None,
                "cadmium": None
            },
            "AdditiveElements": {
                "calcium": "oil_analysis_results.samples[].element_analysis_ppm.calcium_ppm",
                "magnesium": "oil_analysis_results.samples[].element_analysis_ppm.magnesium_ppm",
                "zinc": "oil_analysis_results.samples[].element_analysis_ppm.zinc_ppm",
                "phosphorus": "oil_analysis_results.samples[].element_analysis_ppm.phosphorus_ppm",
                "barium": "oil_analysis_results.samples[].element_analysis_ppm.barium_ppm"
            }
        }
    ],
    "AnalysisResults": {
        "oilRating": "oil_analysis_results.samples[-1].usage_information.lubricant_condition",
        "unitRating": None,
        "diagnosis":  "oil_analysis_results.diagnosis_remarks.remarks",
        "recommendations": None,
        "actionRequired": None,
        "nextSampleDue": None,
        "sampleFrequency": None
    },
    "QualityAndCompliance": {
        "reportStatus": None,
        "report ": None,
        "frequency": None,
        "dueStatus": None
    }
}
