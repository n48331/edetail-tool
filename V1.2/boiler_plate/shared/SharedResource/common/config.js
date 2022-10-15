var config = {
  project: "1234_AB",
  slides: {
    s1: {
      name: "s1",
      zipFile: "1234_AB_S1_Slide.zip",
    },
    s2: {
      name: "s2",
      zipFile: "1234_AB_S2_Slide.zip",
    },
    s3: {
      name: "s3",
      zipFile: "1234_AB_S3_Slide.zip",
    },
    s4: {
      name: "s4",
      zipFile: "1234_AB_S4_Slide.zip",
    },
    s5: {
      name: "s5",
      zipFile: "1234_AB_S5_Slide.zip",
    },
    s6: {
      name: "s6",
      zipFile: "1234_AB_S6_Slide.zip",
    },
    s7: {
      name: "s7",
      zipFile: "1234_AB_S7_Slide.zip",
    },
  },
  coreflow: {
    /*First flow should have all the slides*/
    f0: {
      content: ["s1", "s2", "s3", "s4", "s5", "s6", "s7"],
      name: "Flow 0",
    },
  },
};
