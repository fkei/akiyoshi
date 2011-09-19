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
                if (!data || data.length < 1) {
                    return;
                }
				for (var i = 0; i < data.length; i++) {
					$(this).tag("dt")
						.tag("a", {href: "#", id: data[i].name}).text(data[i].name).click(function() {
                            $.akiyoshi.content.graph($(this).attr("id"));
                        }).gat()
                        .gat();
				}
			})
            .gat()
			;
        });
    };

    this.group = function(id, category) {
        $.akiyoshi.group.category("server", function(err, data) {
            if (err) {
                return alert(err); // TODO
            }
            $("#" + id)
            .tagset("blockquote").text("Group - " + category).gat()
            .tag("dl").next(function() {
                if (!data || data.length < 1) {
                    return;
                }
				for (var i = 0; i < data.length; i++) {
					$(this).tag("dt")
						.tag("a", {href: "#", id: data[i].name}).text(data[i].name).click(function() {
                            $.akiyoshi.content.info("main", $(this).attr("id"));
                            $.akiyoshi.action.update([
                                {name:"Home", link:"/"},
                                {name:"Group - " + $(this).attr("id")}
                            ])
                        }).gat()
					    .gat();
				}
			})
            .gat()
            ;
        });
    };
});