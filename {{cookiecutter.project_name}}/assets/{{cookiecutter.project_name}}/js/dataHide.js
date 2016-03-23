$(function() {
	$('[data-hide]').click(function() {
		var id = $(this).attr('data-hide');
		var delay = parseInt($(this).attr('data-hide-delay')) || 0;
		var animation = $(this).attr('data-hide-animation') || 'slide';
		var direction = $(this).attr('data-hide-direction') || 'left';
		var easing = $(this).attr('data-hide-easing') || "easieEaseInQuart";
		var timing = parseInt($(this).attr('data-hide-timing')) || 200;
		var option = { 
			direction: direction,
			easing: easing,
			duration: timing
		};

		$('#' + id).delay(delay).hide(animation, option);
	});	
});