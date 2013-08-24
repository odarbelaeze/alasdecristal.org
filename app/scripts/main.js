require.config({
    paths: {
        jquery: '../bower_components/jquery/jquery',
        bootstrap: 'vendor/bootstrap',
        underscore: '../bower_components/underscore/underscore',
        marked: '../bower_components/marked/lib/marked'
    },
    shim: {
        bootstrap: {
            deps: ['jquery'],
            exports: 'jquery'
        }
    }
});

require(['app', 'jquery', 'marked', 'bootstrap', 'underscore'], function (app, $, marked) {
    'use strict';
    // use app here

    if ($('#team').size()) {
        $.get('/templates/template_team.html', function (template) {
            var teamTemplate = _.template(template);
            $.getJSON('data/team.json', function (data) {
                _.each(data, function (team) {
                    var teamInner = teamTemplate({ team : team });
                    $('#team').append(teamInner);
                });
            });
        });
    }

    if ($('#featured').size()) {
        $.get('/templates/template_product.html', function (template) {
            var productTemplate = _.template(template);
            $.getJSON('/data/new_products.json', function (data) {
                $('#featured').append(productTemplate({ products: data }));
                $('.carousel-inner').each(function () {
                    $(this).children('.item:first').addClass('active');
                });
            });
        });
    }

    if ($('#products').size()) {
        $.get('/templates/template_product.html', function (template) {
            var productTemplate = _.template(template);
            $.getJSON('/data/products.json', function (data) {
                var i = 0;
                while(i < data.length) {
                    $('#products').append(productTemplate({ products: data.slice(i, i + 3) }));
                    $('.carousel-inner').each(function () {
                        $(this).children('.item:first').addClass('active');
                    });
                    i += 3;
                }
            });
        });
    }

    if ($('#hintsaccordion').size()) {
        $.get('/templates/template_hint.html', function (template) {
            var hintTemplate = _.template(template);
            $.getJSON('/data/hints.json', function (data) {
                console.log(data);
                _.each(data, function (hints) {
                    var hintInner = hintTemplate({ hints: hints, parent: 'hintsaccordion' });
                    $('#hintsaccordion').append(hintInner);
                });
            });
        });
    }

    console.log(marked('**I\'m using marked'));

});
