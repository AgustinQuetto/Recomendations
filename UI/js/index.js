$(window).ready(() => {
	var left, width, cont = "#q-cont";
	$('span').click(function(){
		$(this).css("background","#5a6");
		$('.re').css("background","#d90");
		next();
	});
	$('.re').click(() => {
		$(".op").css("background","#d90");
		$('.re').css("background","#5a6");
		$(cont).css("left", "0px");
	});
	function next() {
		width = $(cont).width()/8;
		left = $(cont).css("left").slice(0,-8)*1;
		left -= width;
		$(cont).css("left", left+"px");
	}
});
