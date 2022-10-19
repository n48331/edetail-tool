var touchEvent = touchEvent();
function isTouchDevice() {
  return "ontouchstart" in window;
}
function touchEvent() {
  if (isTouchDevice()) return "touchend";
  else return "click";
}
var config = {
  project: "11052_Tremfya",
  slides: {
    s1: {
      name: "s1",
      zipFile: "11052_Tremfya_S1_Lasting_consistent_relief.zip",
    },
    s2: {
      name: "s2",
      zipFile: "11052_Tremfya_S2_Raise_the_bar_in_psoriasis_treatment.zip",
    },
    s3: {
      name: "s3",
      zipFile: "11052_Tremfya_S3_Long_term_and_complete_skin_clearance.zip",
    },
    s4: {
      name: "s4",
      zipFile: "11052_Tremfya_S4_Why_Tremfya_instead.zip",
    },
    s5: {
      name: "s5",
      zipFile: "11052_Tremfya_S5_PsO_goes_beyond_skin.zip",
    },
    s6: {
      name: "s6",
      zipFile: "11052_Tremfya_S6_Staying_on_Tremfya_long_term.zip",
    },
    s7: {
      name: "s7",
      zipFile: "11052_Tremfya_S7_Lasting_consistent_relief.zip",
    },
    s8: {
      name: "s8",
      zipFile: "11052_Tremfya_S8_Study_designs.zip",
    },
    s9: {
      name: "s9",
      zipFile: "11052_Tremfya_S9_Study_designs.zip",
    },
    s10: {
      name: "s10",
      zipFile: "11052_Tremfya_S10_Study_designs.zip",
    },
    s11: {
      name: "s11",
      zipFile: "11052_Tremfya_S11_Study_designs.zip",
    },
    s12: {
      name: "s12",
      zipFile: "11052_Tremfya_S12_Study_designs.zip",
    },
    s13: {
      name: "s13",
      zipFile: "11052_Tremfya_S13_SmPC.zip",
    },
  },
  coreflow: {
    /*First flow should have all the slides*/
    f0: {
      content: [
        "s1",
        "s2",
        "s3",
        "s4",
        "s5",
        "s6",
        "s7",
        "s8",
        "s9",
        "s10",
        "s11",
        "s12",
        "s13",
      ],
      name: "Flow 0",
    },
    f1: {
      content: ["s8"],
      name: "Flow 1",
    },
  },
  // List of slides that contains carousel
  carSlide: ["s4"],
};
