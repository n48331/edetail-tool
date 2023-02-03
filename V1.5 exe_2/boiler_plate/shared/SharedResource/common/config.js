var touchEvent = touchEvent();
function isTouchDevice() {
	return 'ontouchstart' in window;
}
function touchEvent() {
	if (isTouchDevice())
		return 'touchend';
	else
		return 'click';
}
var config = {
    "project": "12149_DARZALEX",
    "slides": {
        "s1": {
            "name": "s1",
            "zipFile": "12149_DARZALEX_S1_opening_slide.zip"
        },
        "s2": {
            "name": "s2",
            "zipFile": "12149_DARZALEX_S2_OS_chart.zip"
        },
        "s3": {
            "name": "s3",
            "zipFile": "12149_DARZALEX_S3_OS_in_subgroups_of_patients.zip"
        },
        "s4": {
            "name": "s4",
            "zipFile": "12149_DARZALEX_S4_OS_in_patient_subgroups_continued.zip"
        },
        "s5": {
            "name": "s5",
            "zipFile": "12149_DARZALEX_S5_PFS_chart.zip"
        },
        "s6": {
            "name": "s6",
            "zipFile": "12149_DARZALEX_S6_security.zip"
        },
        "s7": {
            "name": "s7",
            "zipFile": "12149_DARZALEX_S7_reference.zip"
        },
        "s8": {
            "name": "s8",
            "zipFile": "12149_DARZALEX_S8_SIL.zip"
        }

    },
    "coreflow": {
        /*First flow should have all the slides*/
        "f0": {
            "content": ["s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8"],
            "name": "Flow 0"
        },
        "f1": {
            "content": [""],
            "name": "Flow 1"
        }
       
    },
    	// List of slides that contains carousel
	"carSlide": ["s8"]
}