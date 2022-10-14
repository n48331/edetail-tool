/*
Tool: Janssen EDetail Flow Framework
Description: This tool helps in creating the flow of the framework. With the help of config file. Features including finding previous slide, next slide, last visited slide.etc. 
Author: Rajesh Varghese
Version: 1.5(QA Tool)(beta) 1.4(Email)(beta) - 1.3.1(Other edetails linking) - 1.3.0(Engage friendly) - 1.2 (SMPC)
*/
var app = {
    var: {
        slides: {},
        coreflow: {},
        project: "",
        currentSlide: "",
        firstflow: "",
        locstorage: {},
        nextslide: "",
        prevslide: "",
        navig: "",
        env: "",
        anchor: "",
        smpcSlidesArr: "",
        fragments: "",
        account: ""
    },
    start: {
        init: function() {
            var e = app,
                t = e.var;
            t.project = config.project, t.slides = config.slides, t.coreflow = config.coreflow, t.currentSlide = currentSlide, config.vaultId && (t.vault = config.vaultId), config.smpcSlides && (t.smpcSlidesArr = config.smpcSlides.content), t.firstflow = Object.keys(config.coreflow)[0], e.rte.check(), e.storage.check(), e.logic.getdirection(t.locstorage.flow, t.currentSlide), null != localStorage.getItem("lastVisited") && (app.var.lastVisited = JSON.parse(localStorage.getItem("lastVisited"))), localStorage.getItem("NGTool") ? t.env = "dev" : t.env = ""
        },
        test: function() {
            localStorage.setItem("NGTool", "yes"), location.reload()
        }
    },
    stop: {
        test: function() {
            localStorage.setItem("NGTool", ""), location.reload()
        }
    },
    logic: {
        getdirection: function(e, t) {
            var o = app,
                a = o.logic;
            flowitm = o.var.coreflow[e].content, a.getNext(flowitm, t), a.getPrev(flowitm, t)
        },
        getIndex: function(e, t) {
            var o;
            return Object.keys(e).map(function(a, i) {
                e[a] !== t || (o = i + 1)
            }), o
        },
        getNext: function(e, t) {
            var o, a = app.var;
            app.logic.getIndex(app.var.locstorage.flow, t);
            e.indexOf(t) == e.length - 1 ? nextslide = "" : (o = e[e.indexOf(t) + 1], nextslide = a.slides[o].zipFile), app.var.nextslide = nextslide
        },
        getPrev: function(e, t) {
            var o, a = app.var;
            0 == e.indexOf(t) ? prevslide = "" : (o = e[e.indexOf(t) - 1], prevslide = a.slides[o].zipFile), app.var.prevslide = prevslide
        }
    },
    rte: {
        check: function(e = config.rteconnect) {
            var t = app.var;
            e && t.slides[t.currentSlide].rteId
        },
        click: function() {
            var e = app.var;
            void 0 !== e.slides[e.currentSlide].rteId && e.slides[e.currentSlide].rteId ? (console.log("RTE is enabled"), com.veeva.clm.getDataForCurrentObject("Account", "ID", function(e) {
                1 == e.success || alert("Please Select an Account to proceed")
            }), com.veeva.clm.getApprovedDocument(app.var.vault, e.slides[e.currentSlide].rteId, function(e) {
                1 == e.success && (emailerid = e.Approved_Document_vod__c.ID, com.veeva.clm.launchApprovedEmail(emailerid, [], function() {}))
            })) : console.log("RTE is not enabled for this slide")
        },
        findId: function(e) {
            alert("findId"), 1 == e.success && (myTemplate = e.Approved_Document_vod__c.ID, com.veeva.clm.getApprovedDocument(app.var.vault, [], app.rte.launch))
        },
        launch: function(e) {
            alert(entered);
            var t = app.var;
            1 == e.success && (com.veeva.clm.launchApprovedEmail(t.slides[t.currentSlide].rteId, [], function() {
                alert("Success")
            }), t.account || alert("Please select the account"))
        }
    },
    setLastVisited: function() {
        var e = app.var,
            t = {};
        (t = JSON.parse(localStorage.getItem(e.project))).lastPresentation = t.presentation, t.lastFlow = t.flow, t.lastSlide = t.slide, localStorage.setItem("lastVisited", JSON.stringify(t))
    },
    setAnchor: function() {
        var e = app.var,
            t = {};
        (t = JSON.parse(localStorage.getItem(e.project))).lastPresentation = t.presentation, t.lastFlow = t.flow, t.lastSlide = t.slide;
        var o = JSON.stringify(t);
        localStorage.setItem(e.project, o)
    },
    setAccount: function() {
        var e = app.var;
        e.account = 0, e.veevaApp.getDataForCurrentObject("Account", "ID", function(t) {
            1 == t.success ? e.account = t.Account.ID : console.log("asd")
        })
    },
    goNextSlide: function() {
        app.var.nextslide ? (app.setLastVisited(), app.goTo(app.var.nextslide, "next")) : console.log("Last Slide")
    },
    goPrevSlide: function() {
        app.var.prevslide ? (app.setLastVisited(), app.goTo(app.var.prevslide, "prev")) : console.log("First Slide")
    },
    goToSlidezip: function(e, t) {
        app.setLastVisited();
        var o = app.var;
        app.storage.setValue(e, t);
        var a = o.slides[t].zipFile;
        app.goTo(a)
    },
    goToLastVisited: function() {
        if (localStorage.getItem("lastVisited")) {
            var e = JSON.parse(localStorage.getItem("lastVisited"));
            app.goToSlidezip(e.lastFlow, e.lastSlide)
        }
    },
    goTo: function(e, t = "") {
        var o;
        if (app.var.locstorage.navig > 10 && "dev" == app.var.env) {
            o = e.slice(0, -4);
            var a = document.getElementById("mainWrapper"),
                i = 0,
                r = setInterval(function() {
                    i > 499 ? (clearInterval(r), document.location = "../" + o + "/" + o + ".html") : (i += 80, "next" == t ? a.style.left = -i + "px" : "prev" == t && (a.style.left = i + "px"))
                }, 5)
        } else com.veeva.clm.gotoSlide("" + e)
    },
	goToPi: function (component) {
		var that = this, v = app.var, flow, slide, flowitm;
		flow = component.getAttributeNode("data-flow").value;
		slide = component.getAttributeNode("data-slide").value;
		console.log('text', slide)
		if (flow && slide) {
			flowitm = v.coreflow[flow].content;
			if (flowitm.includes(slide)) {
				if (app.var.currentSlide !== 's9') {
					app.setParentSlide(1);
				}
				app.goToSlidezip(flow, slide);
			} else {
				console.log("Slide " + slide + " is not present in the flow " + flow);
			}
		}
	},
	setParentSlide: function (act) {
		if (act == 1) {
			localStorage.setItem('parentSlide', app.var.currentSlide);
		} else {
			localStorage.setItem('parentSlide', '');
		}
	},
	 goToParentSlide: function () {
		// console.log('aaaaa');
		if (localStorage.getItem('parentSlide') != '') {
			// console.log('aaaaa');
			var slide = localStorage.getItem('parentSlide');
			var flow = 'f0';
			app.setParentSlide(0);
			app.goToSlidezip(flow, slide);
		}
	},
	setSubParentSlide: function (act) {
		if (act == 1) {
			localStorage.setItem('goToHome1', app.var.currentSlide);
		} else {
			localStorage.setItem('goToHome1', '');
		}
	},
    gotoSubParent: function () {
		// console.log('aaaaa');
		if (localStorage.getItem('goToHome1') != '') {
			// console.log('aaaaa');
			var slide = localStorage.getItem('goToHome1');
			var flow = 'f0';
			app.setSubParentSlide(0);
			app.goToSlidezip(flow, slide);
		}
	},
    setsub_slide_localstorage: function (sub_slide) {
		if (sub_slide != null && sub_slide != '' && sub_slide != 0) {
			localStorage.setItem("goToPrev", sub_slide);
		}else {
			localStorage.setItem("goToPrev", '');
		}
	},
	Checksub_slide_localstorage: function (goToHome) {
		if (goToHome != '' && goToHome != null)   {
			// var item = goToHome - 1;
			$(".item").removeClass('active');
			$(".item:nth-child("+goToHome+")").addClass('active');
			// console.log('aaaaaaaa', goToHome)
			app.setsub_slide_localstorage(0);	
		}
	},
	getActiveItem: function () {
		$('.item').each( function(){
			if ($(this).hasClass('active')){
			  var X = $(this).find('section').attr('class');
			  var activeItem = X.split('-')[1]
			  app.setsub_slide_localstorage(activeItem);	
			  // console.log(X);
			}
			
			// console.log($(this));
		  });
	},
	
	goToHomeButton: function (component) {
		var that = this, v = app.var, flow, slide, flowitm;
		flow = component.getAttributeNode("data-flow").value;
		slide = component.getAttributeNode("data-slide").value;
		var sub_slide = component.getAttributeNode("sub_slide").value;
		app.setsub_slide_localstorage(sub_slide);		
		if (flow && slide) {
			var goToHome = v.currentSlide;
			localStorage.setItem("goToHome1", goToHome);
			flowitm = v.coreflow[flow].content;
            app.storage.setValue(flow, slide);
			//console.log(flowitm)
			//console.log(flowitm.includes("s030"));
			if (flowitm.includes(slide)) {
				var zipFile = v.slides[slide].zipFile;
				app.goTo(zipFile, '', goToHome);
			} else {
				console.log("Slide " + slide + " is not present in the flow " + flow);
			}
		}
	},
    goToButton: function(e) {
        var t, o, a = app.var;
        t = e.getAttributeNode("data-flow").value, o = e.getAttributeNode("data-slide").value, t && o && (a.coreflow[t].content.includes(o) ? app.goToSlidezip(t, o) : console.log("Slide " + o + " is not present in the flow " + t))
    },
    goToDifferentSlide: function(e, t = "") {
        com.veeva.clm.gotoSlide("" + e, t)
    },
    setAnchor: function(e) {
        var t = app.var;
        t.anchor = t.currentSlide, this.goToButton(e)
    },
    storage: {
        setValue: function(e, t) {
            var o, a, i, r = app.var;
            o = JSON.parse(localStorage.getItem(r.project)), (a = {}).presentation = o.presentation, a.flow = e, a.slide = t, r.anchor ? a.anchor = r.anchor : a.anchor = o.anchor, a.navig = o.navig, a.lastSlide = o.currentSlide, i = JSON.stringify(a), localStorage.setItem(r.project, i), r.locstorage = a
        },
        check: function() {
            var e, t = app.var,
                o = navigator.userAgent;
            if (app.var.navig = o.indexOf("Chrome"), null === localStorage.getItem(t.project)) {
                (i = {}).presentation = t.project, i.flow = t.firstflow, i.slide = t.currentSlide, i.anchor = t.anchor, i.lastSlide = t.currentSlide, i.navig = t.navig;
                var a = JSON.stringify(i);
                localStorage.setItem(t.project, a), t.locstorage = i
            } else if (e = JSON.parse(localStorage.getItem(t.project)), flowitm = t.coreflow[e.flow].content, t.currentSlide == e.slide && flowitm.includes(t.currentSlide)) t.locstorage = e, t.lastVisited = e.lastSlide;
            else if (flowitm.includes(t.currentSlide)) {
                (i = {}).presentation = e.presentation, i.flow = e.flow, i.slide = t.currentSlide, i.navig = e.navig, i.lastSlide = t.currentSlide, t.anchor ? i.anchor = t.anchor : i.anchor = e.anchor;
                a = JSON.stringify(i);
                localStorage.setItem(t.project, a), t.locstorage = i
            } else {
                var i;
                (i = {}).presentation = e.presentation, i.flow = t.firstflow, i.slide = t.currentSlide, i.anchor = t.anchor, i.navig = e.navig, t.anchor ? i.anchor = t.anchor : i.anchor = e.anchor;
                a = JSON.stringify(i);
                localStorage.setItem(t.project, a), t.locstorage = i
            }
        },
        test: function() {
            var e = app.var;
            localStorage.customPresentation && "{}" !== localStorage.customPresentation && (e.customsavedslides = JSON.parse(localStorage.getItem("presentation")), Object.keys(e.customsavedslides).map(function(t, o) {
                e.slideshow[Name] = {}, e.slideshow[Name] = e.customsavedslides[t]
            }))
        }
    },
    bindSwipe: function() {
        $(".mainWrapper").swipe({
            swipe: function(e, t, o, a, i, r) {
                var l = app,
                    n = 1;
                "left" === t ? n < len && (n++, idName = l.getNext(l.var.slideshow[currentSlide].content, slide), l.goToSlide(n, idName)) : "right" === t && n > 1 && (n--, idName = l.getPrev(l.var.slideshow[currentSlide].content, slide), l.goToSlide(n, idName))
            }
        })
    },
    isTouchDevice: function() {
        return "ontouchstart" in window
    },
    init: function() {
        this.start.init()
    }
};
app.init();