$(function() {
	$('[data-show]').click(function() {
		var id = $(this).attr('data-show')
		var delay = parseInt($(this).attr('data-show-delay')) || 300;
		var animation = $(this).attr('data-show-animation') || 'slide';
		var direction = $(this).attr('data-show-direction') || 'right';
		var easing = $(this).attr('data-show-easing') || "easieEaseOutQuart";
		var timing = parseInt($(this).attr('data-show-timing')) || 200;
		var option = { 
			direction: direction,
			easing: easing,
			duration: timing
		};
		$('#' + id).delay(delay).show(animation, option);
	});
});