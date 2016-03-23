$(function() {
	// if ($(window).width() > 768) {
	$('.dropdown-animated').each(function() {
		$(this).on('show.bs.dropdown', function(){
		    $(this).find('.dropdown-menu').first().stop(true, true).slideToggle(100);
		});
		$(this).on('hide.bs.dropdown', function(){
		    $(this).find('.dropdown-menu').first().stop(true, true).slideToggle(100);
		});
	});
		
	// }
});