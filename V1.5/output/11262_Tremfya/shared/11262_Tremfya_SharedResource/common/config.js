var config = {
  project: "11262_Tremfya",
  slides: {
    s1: {
      name: "s1",
      zipFile:
        "11262_Tremfya_S1_Safety_a_key_factor_when_choosing_a_biologic_for_your_psa_patient.zip",
    },

    s2: {
      name: "s2",
      zipFile: "11262_Tremfya_S2_Rationale.zip",
    },

    s3: {
      name: "s3",
      zipFile:
        "11262_Tremfya_S3_What_impact_do_treatment_related_adverse_events_have_on_patients.zip",
    },

    s4: {
      name: "s4",
      zipFile:
        "11262_Tremfya_S4_A_deeper_look_at_the_moa_and_main_safety_risks_of_biologics_in_psa.zip",
    },

    s5: {
      name: "s5",
      zipFile:
        "11262_Tremfya_S5_Tremfya_an_il-23_inhibitor_with_a_safety_profile_comparable_to_placebo.zip",
    },

    s6: {
      name: "s6",
      zipFile: "11262_Tremfya_S6_Tremfyas_strong_efficacy_and_good_safety.zip",
    },

    s7: {
      name: "s7",
      zipFile: "11262_Tremfya_S7_SmPC.zip",
    },

    s8: {
      name: "s8",
      zipFile: "11262_Tremfya_S8_References.zip",
    },
  },
  coreflow: {
    /*First flow should have all the slides*/
    f0: {
      content: ["s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8"],
      name: "Flow 0",
    },
  },
  carSlide: ["s5"],
};
