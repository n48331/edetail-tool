$(document).ready(function () {
  if (app.isTouchDevice()) {
    touchEvent = "touchend";
  } else {
    touchEvent = "click";
  }

  /* Anchor Slides Start */
  var getAnchorSlide = app.var.locstorage.anchor;
  if (getAnchorSlide) {
    $(".close_icon").attr("data-slide", getAnchorSlide);
  } else {
    $(".close_icon").attr("data-slide", "s1");
  }
  /* Anchor Slides stop */

  // $('#bottommenu2_s57').unbind().bind('touchstart tap', function(){
  //   $("#mainWrapper").css({
  //     'background': 'url("../shared/5450_TR_SharedResource/img/main2.jpg")',
  //     'background-size': 'cover'
  //   });
  // });
  // $('.bottommenu2').unbind().bind('tap', function(){
  //     app.var.slideTrackArr = (localStorage.getItem('slideTrackArr'))? JSON.parse(localStorage.getItem('slideTrackArr')): []
  //     app.var.slideTrackArr.push(app.var.currentSlide);
  //     localStorage.setItem('slideTrackArr',JSON.stringify(app.var.slideTrackArr));
  //     // alert(app.var.slideTrackArr);
  //     app.goTo(config.slides.s57.zipFile);
  // });
  // $('.bottommenu1').unbind().bind('touchstart tap', function(){
  //   app.goTo(config.slides.s2.zipFile);
  // });
  // $('.bottommenu2').unbind().bind('touchstart tap', function(){
  //   console.log("hhh")
  //   app.goTo(config.slides.s3.zipFile);
  // });
  // $('.bottommenu3').unbind().bind('touchstart tap', function(){
  //   app.goTo(config.slides.s1.zipFile);
  // });
  $(".nav_s7")
    .unbind()
    .bind(touchEvent, function () {
      // console.log("hi");
      document.location =
        "../shared/1234_AB_SharedResource/pdf/Erleada-FullSmPC-10.02.2022-II-017.pdf";
    });
});

// Play Video here
function openModalVideo(id) {
  setTimeout(function () {
    var identifier = id;
    console.log("opening modal: " + id);
    $(".modal").removeClass("visible");
    setTimeout(function () {
      $(".modal").removeClass("active");
    }, 300);
    setTimeout(function () {
      $("#modal-modal_" + identifier).addClass("active");
      setTimeout(function () {
        $("#modal-modal_" + identifier).addClass("visible");
      }, 0);
    }, 310);

    if (isEngage) {
      $("video").hide();
      $(".video_bg").show();
      $(".video_bg").on(touchEvent, function () {
        closeModal(identifier);
      });
    } else {
      $("*[vidplayer]").on(touchEvent, function () {
        $("#neromuscular").get(0).play();
      });
      $("#neromuscular").on(touchEvent, function () {
        $("#neromuscular").get(0).pause();
        $(".video_bg").show();
        $(".video_bg").on(touchEvent, function () {
          closeModal(identifier);
        });
      });
    }
  }, 50);
}
function closeModal(id) {
  var identifier = id;
  $("#modal-modal_" + identifier).removeClass("visible");
  $("#modal-modal_" + identifier + " video").each(function () {
    this.load();
  });
  setTimeout(function () {
    $("#modal-modal_" + identifier).removeClass("active");
  }, 300);
  $(".video_bg").css("display", "none");
}
// Play Video here
