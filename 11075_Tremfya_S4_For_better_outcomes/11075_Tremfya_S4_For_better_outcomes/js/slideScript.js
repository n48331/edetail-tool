$(document).ready(function () {

	$(".right_arrow1").click(function(){
		$(".popup_box_2").show();
        // $(".popup_box_1").hide();
        
	});
	
    $(".left_arrow2").click(function(){
		$(".popup_box_1").show();
        $(".popup_box_2").hide();
        
	});
    $(".left_arrow22").click(function(){		
        $(".popup_box_1").hide();
		$(".section-2").show();
        
	});
    $(".left_arrow33").click(function(){		
        $(".popup_box_1").hide();
		$(".section-3").show();
        
	});
	$(".s4_popup3").click(function(){
		$(".popup_box_2").show();
		// $(".popup_box_1").hide();
	});
	$(".popup_box_2 .close1").click(function(){
		$(".popup_box_1 ").show();
		$(".popup_box_2").hide();
		
	});
	
})