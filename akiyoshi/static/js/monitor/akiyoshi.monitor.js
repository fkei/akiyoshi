$.akiyoshi.addHandler("monitor", new function() {
	this.info = function(host, param, callback) {
        host = host || "";
        $.akiyoshi.ajax.async({
            type: "GET",
            url: "/monitor/" + host,
            data: param || ""
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
