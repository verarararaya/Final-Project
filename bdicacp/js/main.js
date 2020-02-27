/*
Author: Dot Themes
*/
(function($) {
    "use strict";

    smoothScroll.init();

    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });


    $('body').scrollspy({
        target: '.navbar-fixed-top'
    });


    $('.navbar-collapse ul li a').click(function() {
        $('.navbar-toggle:visible').click();
    });


    $(window).scroll(function(event) {
        Scroll();
    });


   	$("a[data-gal^='prettyPhoto']").prettyPhoto(); 


    $(document).ready(function() {
        $("#owl-example").owlCarousel();
        var owl = $("#fn-feedbacks");
        owl.owlCarousel({
            items: 3,
            itemsDesktop: [1000, 2],
            itemsDesktopSmall: [900, 1],
            itemsTablet: [600, 1],
            itemsMobile: false
        });

        /* ==========  START GOOGLE MAP ========== */
        google.maps.event.addDomListener(window, 'load', init);

        function init() {
            var myLatLng = new google.maps.LatLng(40.70968790739889, -74.06913757324219);

            var mapOptions = {
                zoom: 15,
                center: myLatLng,
                disableDefaultUI: true,
                scrollwheel: false,
                navigationControl: true,
                mapTypeControl: false,
                scaleControl: false,
                draggable: true,

                styles: [{
                    featureType: 'water',
                    stylers: [{
                        color: '#ECC731'
                    }, {
                        visibility: 'on'
                    }]
                }, {
                    featureType: 'landscape',
                    stylers: [{
                        color: '#f2f2f2'
                    }]
                }, {
                    featureType: 'road',
                    stylers: [{
                        saturation: -100
                    }, {
                        lightness: 45
                    }]
                }, {
                    featureType: 'road.highway',
                    stylers: [{
                        visibility: 'simplified'
                    }]
                }, {
                    featureType: 'road.arterial',
                    elementType: 'labels.icon',
                    stylers: [{
                        visibility: 'off'
                    }]
                }, {
                    featureType: 'administrative',
                    elementType: 'labels.text.fill',
                    stylers: [{
                        color: '#444444'
                    }]
                }, {
                    featureType: 'transit',
                    stylers: [{
                        visibility: 'off'
                    }]
                }, {
                    featureType: 'poi',
                    stylers: [{
                        visibility: 'off'
                    }]
                }]
            };
            var mapElement = document.getElementById('map-canvas');
            var map = new google.maps.Map(mapElement, mapOptions);
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(40.70968790739889, -74.06913757324219),
                map: map,
                icon: 'img/icons/map-marker.png',
            });
        }
        // ========== END GOOGLE MAP ========== //
    });


    $(window).load(function() {
        'use strict';
        var $gallery_selectors = $('.gallery-filter >li>a');
        var $gallery = $('.gallery-items');
        $gallery.isotope({
            itemSelector: '.gallery-item',
            layoutMode: 'fitRows'
        });

        $gallery_selectors.on('click', function() {
            $gallery_selectors.removeClass('active');
            $(this).addClass('active');
            var selector = $(this).attr('data-filter');
            $gallery.isotope({
                filter: selector
            });
            return false;
        });
    });

})(jQuery);