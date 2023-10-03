'use strict';

document.addEventListener('DOMContentLoaded', function () {
	/* ==================================================
         MODAL VIDEO
    ================================================== */
	new ModalVideo('.video-btn');

	/* ==================================================
         CHANGING NAVBAR STYLING ON SCROLL
    ================================================== */
	window.addEventListener('scroll', function () {
		let windowScroll = document.scrollingElement.scrollTop;
		if (windowScroll >= 1) {
			document.querySelector('.header.header-animated').classList.add('active');
		} else {
			document.querySelector('.header.header-animated').classList.remove('active');
		}
	});

	/* =====================================================
        SHOW/HIDE NAVBAR ON SCROLLING
    ===================================================== */
	let c = 0,
		currentScrollTop = 0;

	window.addEventListener('scroll', function () {
		let a = document.body.parentNode.scrollTop;
		let b = document.querySelector('.header').offsetHeight;

		currentScrollTop = a;

		if (c < currentScrollTop && a > b + b) {
			document.querySelector('.header').classList.add('scrollUp');
		} else if (c > currentScrollTop && !(a <= b)) {
			document.querySelector('.header').classList.remove('scrollUp');
		}
		c = currentScrollTop;
	});

	/* ===============================================================
		TESTIMONIALS SLIDER
	=============================================================== */
	var testimonialsSlider = new Swiper('.testimonials-slider', {
		slidesPerView: 1,
		spaceBetween: 30,
		loop: true,
		autoplay: {
			delay: 4000,
		},
		pagination: {
			el: '.swiper-pagination',
			type: 'bullets',
		},
	});

	/* ===============================================================
		DISABLE UNWORKED ANCHORS
	=============================================================== */
	document.querySelectorAll('a[href="#').forEach((el) => {
		el.addEventListener('click', function (e) {
			e.preventDefault();
		});
	});

	/* =====================================================
        SCROLL TOP BUTTON [SHOW & HIDE & CLICKING]
    ===================================================== */
	const scrollTopBtn = document.querySelector('#scrollTop');
	if (scrollTopBtn) {
		scrollTopBtn.addEventListener('click', function () {
			window.scrollTo(0, 0);
		});

		window.addEventListener('scroll', function () {
			if (window.pageYOffset >= 1000) {
				scrollTopBtn.classList.add('active');
			} else {
				scrollTopBtn.classList.remove('active');
			}
		});
	}
});
