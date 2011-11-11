$.akiyoshi.addHandler("rrd", new function() {
	this.host = function(id, host, callback) {
        $.akiyoshi.ajax.async({
            type: "GET",
            url: "/rrd/"+host
        })
        .success(function(data) {
            callback(null, data);
        })
		.error(function(jqXHR, textStatus, errorThrown) {
			callback(textStatus);
		})
		.end()
		;
    }
    ;
});
