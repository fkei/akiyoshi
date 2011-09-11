$.akiyoshi.addHandler("manager", new function() {
	this.info = function(callback) {
		$.akiyoshi.ajax.async({
			type: "GET",
			url: "/manager/node"
		})
		.success(function(data) {
			callback(null, data);
		})
		.error(function(jqXHR, textStatus, errorThrown) {
			callback(textStatus);
		})
		.end()
		;
	};
});
