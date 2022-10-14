var config = {
  project: "1453_DA",
  slides: {
  
        s1: {
        name: "s1",
        zipFile: "1234_AB_S1_hi_hello.zip",
        },
        
        s2: {
        name: "s2",
        zipFile: "1234_AB_S2_good_bye.zip",
        },
        
        s3: {
        name: "s3",
        zipFile: "1234_AB_S3_have_a_nice_day.zip",
        },
        
        s4: {
        name: "s4",
        zipFile: "1234_AB_S4_what_a_good_day.zip",
        },
        
  },
  coreflow: {
    /*First flow should have all the slides*/
    f0: {
      content: ["s1","s2","s3","s4",],
      name: "Flow 0",
    },
   
  },

};

	