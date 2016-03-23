$(window).load(function() {
	$(".show-me").each(function() {
		$(this).delay(400).animate({opacity: '1', top: '0'}, 300, $.easieEaseOutQuint);
	})
	$(".show-me-after").each(function() {
		$(this).delay(500).animate({opacity: '1', top: '0'}, 300, $.easieEaseOutQuint);
	})
	$(".show-me-delay").each(function() {
		$(this).delay(100).animate({opacity: '1', top: '0'}, 300, $.easieEaseOutQuint);
	})
});