$(document).ready(function () {
	$(".bottommenu5").click(function(){
		$(".s1_popup_box_1").show();
		$(".bottommenu1, .bottommenu2, .bottommenu3, .bottommenu4, .bottommenu5, .bottommenu6").hide();
	});
	$(".s1_popup_box_1 .close").click(function(){
		$(".s1_popup_box_1").hide();
		$(".bottommenu1, .bottommenu2, .bottommenu3, .bottommenu4, .bottommenu5, .bottommenu6").show();
	});
	$(".bottommenu6").click(function(){
		$(".s1_popup_box_2").show();
		$(".bottommenu1, .bottommenu2, .bottommenu3, .bottommenu4, .bottommenu5, .bottommenu6").hide();
	});
	$(".s1_popup_box_2 .popup2_close").click(function(){
		$(".s1_popup_box_2").hide();
		$(".bottommenu1, .bottommenu2, .bottommenu3, .bottommenu4, .bottommenu5, .bottommenu6").show();
	});	
	
	
})