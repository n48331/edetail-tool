$(document).ready(function(){
    $(".page2_popup").click(function () {
		$(".page2_popup_box").show();
	});
	$(".page2_popup_box .close").click(function () {
		$(".page2_popup_box").hide();
	});
	$(".page4_popup").click(function () {
		$(".page4_popup_box").show();
	});
	$(".page4_popup_box .close").click(function () {
		$(".page4_popup_box").hide();
	});
	$(".page7_popup1").click(function () {
		$(".page7_popup1_box").show();
	});
	$(".page7_popup1_box .close").click(function () {
		$(".page7_popup1_box").hide();
	});
	$(".page7_popup2").click(function () {
		$(".page7_popup2_box").show();
	});
	$(".page7_popup2_box .close").click(function () {
		$(".page7_popup2_box").hide();
	});
	$(".page7_popup3").click(function () {
		$(".page7_popup3_box").show();
	});
	$(".page7_popup3_box .close").click(function () {
		$(".page7_popup3_box").hide();
	});
    $(".page11_popup1").click(function () {
		$(".page11_popup1_box").show();
	});
	$(".page11_popup1_box .close").click(function () {
		$(".page11_popup1_box, .page11_popup2_box").hide();
	});
	$(".page11_popup2").click(function () {
		$(".page11_popup2_box").show();
	});
	$(".page11_popup2_box .close").click(function () {
		$(".page11_popup2_box, .page11_popup1_box").hide();
	});
    $(".page15_popup1").click(function () {
		$(".page15_popup1_box").show();
	});
	$(".page15_popup1_box .close").click(function () {
		$(".page15_popup1_box, .page15_popup2_box").hide();
	});
	$(".page15_popup2").click(function () {
		$(".page15_popup2_box").show();
	});
	$(".page15_popup2_box .close").click(function () {
		$(".page15_popup2_box, .page15_popup1_box").hide();
	});


	$(".popup_right_arrow").click(function () {
		$(".page11_popup1_box").hide();
		$(".page11_popup2_box").show();
	});
	$(".popup_left_arrow").click(function () {
		$(".page11_popup2_box").hide();
		$(".page11_popup1_box").show();
	});
	

    $(".page16_popup1").click(function () {
		$(".page16_popup1_box").show();
	});
	$(".page16_popup1_box .close").click(function () {
		$(".page16_popup1_box").hide();
	});
	$(".page16_popup2").click(function () {
		$(".page16_popup2_box").show();
	});
	$(".page16_popup2_box .close").click(function () {
		$(".page16_popup2_box").hide();
	});
});