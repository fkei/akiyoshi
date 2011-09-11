$.akiyoshi.addHandler("content", new function() {
	this.info = function(id) {
		$.akiyoshi.manager.info(function(err, data) {
			if (err) {
				return alert("TODO err");
			}
            $("#"+id)
            .tagset("table", {class: "zebra-striped", id: "servers-table"})
                .tag("thead")
                    .tag("tr")
                        .tag("th", {class: "header"}).text("#").gat()
                        .tag("th", {class: "yellow header headerSortDown"}).text("Host").gat()
                        .tag("th", {class: "blue header headerSortDown"}).text("Status").gat()
                        .tag("th", {class: "green header headerSortDown"}).text("View").gat()
                    .gat()
                .gat()
                .tag("tbody")
                    .next(function() {
                        for (var i = 0; i < data.length; i++) {
                            $(this)
                            .tag("tr")
                                .tag("td").text(i).gat()
                                .tag("td", {class:"host"}).text(data[i].name).gat()
                                .tag("td").text(data[i].control ? "Managed" : "Unmanaged").gat()
                                .tag("td")
                                    .tag("button", {class: "btn info"}).click(function() {
                                        var host = $(this).closest('tr').children("td:eq(1)")[0].firstChild.data;
                                        $.akiyoshi.rrd.host("content", host, function(err, result) {
                                            // template view
                                            $("#"+id)
                                            .tagset("div", {id:"graph-host"})
                                                .tag("div", {class: "row"})
                                                    .next(function() {
                                                        for (var key in result) {
                                                            $(this)
                                                            .tag("div", {class: "span4 columns"})
                                                                .tag("h3")
                                                                    .tag("a", {href: result[key].url}).text(key).gat()
                                                                    .tag("button", {style: "margin-left:23px;", class: "btn small"}).text("reload").gat()
                                                                .gat()
                                                            .gat()
                                                            ;
                                                        }
                                                    })
                                                .gat()
                                            .gat()
                                            ;
                                        });
                                    }).text("Graph").gat()
                                .gat()
                            .gat()
                            ;
                        }
                    })
                    .gat()
                .gat()
            .gat()
            ;
            $("table#servers-table").tablesorter({sortList: [[1,0]]});
		});
	};
});
