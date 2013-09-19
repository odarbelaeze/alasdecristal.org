require.config({
    paths: {
        jquery: '../bower_components/jquery/jquery',
        underscore: '../bower_components/underscore/underscore',
        marked: '../bower_components/marked/lib/marked',
        bootstrapAffix: '../bower_components/sass-bootstrap/js/affix',
        bootstrapAlert: '../bower_components/sass-bootstrap/js/alert',
        bootstrapButton: '../bower_components/sass-bootstrap/js/button',
        bootstrapCarousel: '../bower_components/sass-bootstrap/js/carousel',
        bootstrapCollapse: '../bower_components/sass-bootstrap/js/collapse',
        bootstrapDropdown: '../bower_components/sass-bootstrap/js/dropdown',
        bootstrapPopover: '../bower_components/sass-bootstrap/js/popover',
        bootstrapScrollspy: '../bower_components/sass-bootstrap/js/scrollspy',
        bootstrapTab: '../bower_components/sass-bootstrap/js/tab',
        bootstrapTooltip: '../bower_components/sass-bootstrap/js/tooltip',
        bootstrapTransition: '../bower_components/sass-bootstrap/js/transition'
    },
    shim: {
        bootstrapAffix: {
            deps: ['jquery']
        },
        bootstrapAlert: {
            deps: ['jquery']
        },
        bootstrapButton: {
            deps: ['jquery']
        },
        bootstrapCarousel: {
            deps: ['jquery']
        },
        bootstrapCollapse: {
            deps: ['jquery']
        },
        bootstrapDropdown: {
            deps: ['jquery']
        },
        bootstrapPopover: {
            deps: ['jquery']
        },
        bootstrapScrollspy: {
            deps: ['jquery']
        },
        bootstrapTab: {
            deps: ['jquery']
        },
        bootstrapTooltip: {
            deps: ['jquery']
        },
        bootstrapTransition: {
            deps: ['jquery']
        }
    }
});

require(['app', 'jquery', 'marked', 'underscore',
         'bootstrapCarousel', 'bootstrapCollapse', 'bootstrapTransition'
    ], function (app, $, marked) {
    'use strict';

    $('.carousel').carousel();

    if ($('#featured').size()) {
        var productTemplate = _.template($('#featured-template').html());
        $.getJSON('../static/data/featured.json', function (data) {
            var tasks = [];
            _.each(data, function (product) {
                var request = $.get('../static/data/products/' + product.id + '.md', function (text) {
                    product.description = marked(text);
                });
                tasks.push(request);
            });
            $.when.apply($, tasks).then(function () {
                var i = 0;

                while (i < data.length) {
                    $('#featured').append(productTemplate({ products: data.slice(i, i + 3) }));
                    i = i + 3;
                }

                $('.carousel-inner').each(function () {
                    $(this).children('.item:first').addClass('active');
                });

                $('.carousel-indicators').each(function () {
                    $(this).children('li:first').addClass('active');
                });

                $('.product-collapser').click(function (evt) {
                    if ($('.collapse.in').size()) {
                        evt.preventDefault();
                        $('.collapse.in').collapse('hide');
                    }
                });

                $('.description-text>dl').addClass('dl-horizontal');
            });
        });
    }

    console.log(app);
    console.log('Running jQuery %s', $().jquery);
});
