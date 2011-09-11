(function($) {
	$.extend({
		akiyoshi: new function() {
			this.addHandler = function(method, fn) {
				this[method] = fn;
				if (fn.hasOwnProperty("init")) {
					this[method].init();
				}
			}
		}
	});
})(jQuery);
