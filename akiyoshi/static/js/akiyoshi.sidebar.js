$.akiyoshi.addHandler("sidebar", new function() {
    this.nodes = function(id) {
        $.akiyoshi.node.list(id, function(err, data) {
            if (err) {
				// TODO Error Handring!!
                return alert(err);
            }
			$("#"+id)
			    .tagset("blockquote").text("Servers").gat()
				.tag("dl")
			    .next(function() {
					for (var i = 0; i < data.length; i++) {
						$(this).tag("dt")
							.tag("a", {href:"/node/"+data[i]}).text(data[i]).gat()
						.gat();
					}
				})
				.gat().end()
			;
			
            
        });
    }
});