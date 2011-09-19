$.akiyoshi.addHandler("group", new function() {
    this.category = function(category, callback) {
        $.akiyoshi.ajax.async({
            type: "GET",
            url: "/group/"+category
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