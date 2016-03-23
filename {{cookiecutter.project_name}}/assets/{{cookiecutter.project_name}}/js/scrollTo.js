$(function() {
	$('[data-scroll-to]').click(function() {
		var id = $(this).attr('data-scroll-to');
		var easing = $(this).attr('data-scroll-easing') || 'easieEaseInOutCirc';
		var offset = $(this).attr('data-scroll-offset') || '0';
		var duration = $(this).attr('data-scroll-duration') || '800';
		$.scrollTo($('#' + id),{
			axis: 'y',
			duration: parseInt(duration),
			offset: parseInt(offset),
			easing: easing
		});
	})
});