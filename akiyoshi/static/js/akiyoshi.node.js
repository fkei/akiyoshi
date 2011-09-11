$.akiyoshi.addHandler("node", new function() {

	this.list = function(id, callback) {
		$.akiyoshi.ajax.async({
			type: "GET",
			url: "/node"
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
