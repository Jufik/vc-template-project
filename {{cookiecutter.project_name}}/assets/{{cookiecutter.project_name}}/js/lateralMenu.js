$(function() {
	$('.open-menu').click(function() {
		$(this).removeClass('collapsed');
		$("#lateralMenu").animate({
			left: 0,
		}, 300, "easieEaseInQuart");
		$('body').addClass('modal-open')
		setTimeout(function() {
			$('.navbar-close').addClass('rotate');
		}, 200);
	});

	$("#lateralMenu li a").click(function(e) {
		$('.open-menu').addClass('collapsed');
		$('.navbar-close').removeClass('rotate'); 
		$("#lateralMenu").animate({
			left: '100%',
		}, 300, "easieEaseInQuart");
		$('body').removeClass('modal-open')
	});	

	$('.navbar-close').click(function() {
		$('.open-menu').addClass('collapsed');
		$(this).removeClass('rotate');
		$("#lateralMenu").animate({
			left: '100%',
		}, 300, "easieEaseInQuart");
		$('body').removeClass('modal-open')
	});
});