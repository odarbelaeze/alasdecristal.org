require.config({
    paths: {
        jquery: '../bower_components/jquery/jquery',
        dynamicFormset: '../bower_components/django-dynamic-formset/src/jquery.formset',
        underscore: '../bower_components/underscore/underscore',
        marked: '../bower_components/marked/lib/marked',
        bootstrapAffix: '../bower_components/sass-bootstrap/js/affix',
        bootstrapAlert: '../bower_components/sass-bootstrap/js/alert',
        bootstrapButton: '../bower_components/sass-bootstrap/js/button',
        bootstrapCarousel: '../bower_components/sass-bootstrap/js/carousel',
        bootstrapCollapse: '../bower_components/sass-bootstrap/js/collapse',
        bootstrapDropdown: '../bower_components/sass-bootstrap/js/dropdown',
        bootstrapModal: '../bower_components/sass-bootstrap/js/modal',
        bootstrapPopover: '../bower_components/sass-bootstrap/js/popover',
        bootstrapScrollspy: '../bower_components/sass-bootstrap/js/scrollspy',
        bootstrapTab: '../bower_components/sass-bootstrap/js/tab',
        bootstrapTooltip: '../bower_components/sass-bootstrap/js/tooltip',
        bootstrapTransition: '../bower_components/sass-bootstrap/js/transition'
    },
    shim: {
        dynamicFormset: {
            deps: ['jquery']
        },
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
        bootstrapModal: {
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

require(['app',
         'jquery',
         'marked',
         'underscore',
         'dynamicFormset',
         'bootstrapCarousel',
         'bootstrapCollapse',
         'bootstrapModal',
         'bootstrapTransition'
    ], function (app, $, marked) {
    'use strict';

    $('.carousel-inner').each(function () {
        $(this).children('.item:first').addClass('active');
    });

    $('.carousel-indicators').each(function () {
        $(this).children('li:first').addClass('active');
    });

    $('.marked').each(function () {
        var $this = $(this);
        if ($this.data('source')) {
            $.get($this.data('source'), function (data) {
                $this.html(marked(data));
                $('.product-description  dl').addClass('dl-horizontal');
            });
        }
        else {
            $this.html(marked($this.text()));
        }
    });
    
    $('.ajax-form').each(function () {
        var $this = $(this);
        $.get($this.data('source'), function (data) {
            $this.html(data);
            $this.submit(function (evt) {

                $.post($this.attr('action'), $this.serialize(), function(data, textStatus, jqXHR) {
                    if (data.search('errorlist') != -1 || data.search('has-error') != -1) {
                        $this.html(data);
                    }
                    else {
                        window.location.replace($this.data('success'));
                    }
                }).done(function () {
                    $('input[type="text"], textarea').addClass('form-control');
                });

                return false;
            });
        }).done(function () {
            $('input[type="text"], textarea').addClass('form-control');
        });
    });

    console.log(app);
    console.log('Running jQuery %s', $().jquery);
});
