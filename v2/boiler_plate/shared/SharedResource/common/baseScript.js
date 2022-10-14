var currentSlide = 0;
$(document).ready(function () {
  if (app.isTouchDevice()) {
    touchEvent = "touchend";
  } else {
    touchEvent = "click";
  }

  $("body").bind("touchmove", function (e) {
    e.preventDefault();
  });

  $(document).swipe({
    //Generic swipe handler for all directions
    swipe: function (
      event,
      direction,
      distance,
      duration,
      fingerCount,
      fingerData
    ) {
      //$(this).text("You swiped " + direction );
      //console.log($(event.target));
      switch (direction) {
        case "left":
          //console.log(app.var);
          if (
            !$("#overlay,#refpopup,#refclose,#api_popup,.not_to_swipe").is(
              ":visible"
            )
          )
            app.goNextSlide();
          break;
        case "right":
          if (
            !$("#overlay,#refpopup,#refclose,#api_popup,.not_to_swipe").is(
              ":visible"
            )
          )
            app.goPrevSlide();
          break;
        default:
          break;
      }
    },
    //Default is 75px, set to 0 for demo so any distance triggers swipe
    threshold: 100,
  });
  /*$('.goToButton').unbind().bind('touchstart tap', function () {
	    app.goToButton(this);
	});*/
  $(document).on(touchEvent, ".goToButton", function () {
    // console.log("fix it");
    app.goToButton(this);
  });
});

function storeToCRM(zipfile, description) {
  var clickStream = {};
  clickStream.Track_Element_Id_vod__c = "" + zipfile;
  clickStream.Track_Element_Description_vod__c = "" + description;
  clickStream.Track_Element_Type_vod__c = "Main Slide";
  com.veeva.clm.createRecord(
    "Call_Clickstream_vod__c",
    clickStream,
    pushDataToCRMDone
  );
}

function pushDataToCRMDone() {
  console.log("tracked");
}

if ("dev" == app.var.env) {
  if (
    ($("body").prepend(
      "<button id='settingOptRV' class='settingOptRV'></button><div class='settingDetail' style='z-index:1; background-color:rgb(255 255 0 / 70%); color:red; position:absolute; padding: 10px; max-width:150px; word-break: break-all;'><h3 style='color:black'>NextGen eDetail</h3>Slide: <b>" +
        app.var.currentSlide +
        "</b><br/>Flow: " +
        app.var.firstflow +
        "<br/><br/>Highlight: <input type='checkbox' id='SettingHighlight'/><br/>SlideNumber: <input type='checkbox'  id='SettingSno'/><br/>AutoPlay: <input type='checkbox' id='SettingPlay'/><br/><br/>Previous Slide: <br/><small style='color:black'>" +
        app.var.prevslide +
        "</small><br/>NextSlide: <br/><small style='color:black'>" +
        app.var.nextslide +
        "</small><br/></div>"
    ),
    $("#bottommenu div").on("click", function () {
      $(this).trigger("tap");
    }),
    $(document).on("click", "#bottommenu div, #infoclose", function () {
      $(this).trigger("tap");
    }),
    null === localStorage.getItem("NextGenEDA"))
  ) {
    var ng = { autoplay: !1, highlight: !1, slideview: !1, other: !1 },
      sjstring = JSON.stringify(ng);
    localStorage.setItem("NextGenEDA", sjstring);
  } else ng = JSON.parse(localStorage.getItem("NextGenEDA"));
  $(document).ready(function () {
    function t(t = 1) {
      1 == t
        ? ($(".goToButton").addClass("hg"),
          $("#bottommenu > div").addClass("hg"))
        : ($(".goToButton").removeClass("hg"),
          $("#bottommenu > div").removeClass("hg"));
    }
    function e() {
      $(".goToButton").each(function () {
        $(this).html($(this).attr("data-slide"));
      });
    }
    function i() {
      setInterval(function () {
        var t = app.var.nextslide;
        app.goTo(t);
      }, 2e3);
    }
    ng.highlight && (t(), $("#SettingHighlight").attr("checked", "true")),
      ng.slideview && (e(), $("#SettingSno").attr("checked", "true")),
      ng.autoplay && (i(), $("#SettingPlay").attr("checked", "true")),
      $("#SettingHighlight").change(function () {
        if (((hgng = ng), this.checked)) {
          var e = confirm("Are you sure to highlight the click buttons?");
          $(this).prop("checked", e), t(), (hgng.highlight = !0);
        } else t(0), (hgng.highlight = !1);
        var i = JSON.stringify(hgng);
        localStorage.setItem("NextGenEDA", i);
      }),
      $("#SettingSno").change(function () {
        if (((snong = ng), this.checked)) {
          var t = confirm("Are you sure to show the slide numbers?");
          $(this).prop("checked", t), e(), (snong.slideview = !0);
        } else snong.slideview = !1;
        var i = JSON.stringify(snong);
        localStorage.setItem("NextGenEDA", i);
      }),
      $("#SettingPlay").change(function () {
        if (((spng = ng), this.checked)) {
          var t = confirm("Are you sure to enable autoplay?");
          $(this).prop("checked", t), i(), (spng.autoplay = !0);
        } else spng.autoplay = !1;
        var e = JSON.stringify(spng);
        localStorage.setItem("NextGenEDA", e);
      }),
      $(".goToButton")
        .unbind()
        .bind("click", function () {
          app.goToButton(this);
        }),
      $("#settingOptRV")
        .unbind()
        .bind("click", function () {
          $(".settingDetail").toggle("slow");
        });
  });
  $("body").css({
    background:
      "linear-gradient(to right, rgb(40, 48, 72), rgb(133, 147, 152))",
    width: "100vw",
    height: "100vh",
  });
}
