/**
 * @fileOverview tag (jQuery plugin)
 * @name jquery.tag.js
 * @author Kei Funagayama <kei.topaz@gmail.com>
 * @license Dual licensed under the MIT or GPL Version 2 licenses.
 * @version 0.1.2
 */
(function($) {
    jQuery.fn.extend({
        /**
         * Add a tag element.
         *
         * before:
         * <div id="hoge">Test</div>
         *
         * script:
         * $("#hoge")
         *     .tag("a",
         *         {"href": "http://example.com/", id: "home", class: "foo bar"},
         *         true)
         *         .tag("span").text("goto home").gat()
         *     .gat()
         * ;
         *
         *
         * after:
         * <div id="hoge">
         *     Test
         *     <a href="http://example.com/" id="home", class="foo bar">
         *         <span>goto home</span>
         *     </a>
         * </div>
         *
         * @param {String} name tag name
         * @param {JSON} options tag attribute
         */
        tag : function(name, options) {
            return this.pushStack(function() {
                var part = '<'+name;
                for (var key in options) {
                    part += ' '+key+'="'+options[key]+'"';
                }
                part+=' >';
                return jQuery(part);
            }());
        },
        /**
         * Add new tag element.
         *
         * before:
         * <div id="hoge">Test</div>
         *
         * script:
         * $("#hoge")
         *     .tag("a",
         *         {"href": "http://example.com/", id: "home", class: "foo bar"},
         *         true)
         *         .tag("span").text("goto home").gat()
         *     .gat()
         * ;
         *
         *
         * after:
         * <div id="hoge">
         *     <a href="http://example.com/" id="home", class="foo bar">
         *         <span>goto home</span>
         *     </a>
         * </div>
         *
         * @param {String} name tag name
         * @param {JSON} options tag attribute
         */
        tagset: function(name, options) {
            var self = this;
            return this.pushStack(function() {
                self.empty();
                var part = '<'+name;
                for (var key in options) {
                    part += ' '+key+'="'+options[key]+'"';
                }
                part+=' >';
                return jQuery(part);
            }());
        },
        /**
         * Add a javascript.
         *
         * script:
         * $("#hoge")
         *     .tag("a",
         *         {"href": "http://example.com/", id: "home", class: "foo bar"},
         *         true)
         *     .gat().next(function() {
         *         alert("ALERT");
         *     })
         * ;
         */
        next: function(callback) {
            var self = this;
            callback.apply(this);
            return self;
        },
        /**
         * Close the element tag.
         */
        gat : function() {
            return this.end().append(this);
        }
    });
})(jQuery);
