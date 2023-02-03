$(document).ready(function(){
    $(".s5_popup1").click(function(){
          $(".popup_box_1").show();
      });
      $(".popup_box_1 .close").click(function(){
          $(".popup_box_1").hide();
      });
      $(".s5_popup2").click(function(){
          $(".popup_box_2").show();
      });
      $(".popup_box_2 .close").click(function(){
          $(".popup_box_2").hide();
      });
      $(".nextSlide").click(function(){
          $(".popup_box_3").show();
        });
        $(".popup_box_3 .prevSlide").click(function(){
            $(".popup_box_3").hide();
            $(".popup_box_2").show();
      });
     
  });
    