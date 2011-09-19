$.akiyoshi.addHandler("content", new function() {
	this.info = function(id, category) {
		$.akiyoshi.node.info(category, function(err, data) {
			if (err) {
				return alert("TODO err");
			}

            $("#"+id)
            .tagset("div", {class:"well", style:"padding: 14px 19px;"})
                .tag("button", {class:"btn"}).text("CPU").gat()
            .gat()
            .tag("table", {class: "zebra-striped", id: "servers-table"})
                .tag("thead")
                    .tag("tr")
                        .tag("th", {class: "header"}).text("#").gat()
                        .tag("th", {class: "yellow header headerSortDown"}).text("Host").gat()
                        .tag("th", {class: "blue header headerSortDown"}).text("Status").gat()
                        .tag("th", {class: "green header headerSortDown"}).text("Action").gat()
                    .gat()
                .gat()
                .tag("tbody")
                    .next(function() {
                        for (var i = 0; i < data.length; i++) {
                            var popup = data[i].notebook || "";
                            popup += "\n\n";
                            for (var j=0; j < data[i].tags.length; j++) {
                                popup += "&nbsp" + data[i].tags[j] + ",&nbsp;";
                            }
                            $(this)
                            .tag("tr")
                                .tag("td").text(i).gat()
                                .tag("td", {class:"host"}).text(data[i].name).mouseover(function(){
                                    // TODO $(this).popover({title:"Infomation",content: content})
                                })
                                .gat()
                                .tag("td").text(data[i].control ? "Managed" : "Unmanaged").gat()
                                .tag("td").next(function() {
                                    $(this)
                                    .tag("span", {class: "label cursor"}).click(function() {
                                        var host = $(this).closest('tr').children("td:eq(1)")[0].firstChild.data;
                                        $.akiyoshi.content.graph(host);
                                    }).text("Graph").gat();

                                    if (data[i].control === false) {
                                        // Unmanaged
                                        $(this)
                                        .tag("span", {class: "label cursor", "data-controls-modal": "modal", "data-backdrop": true, "data-keyboard": true}).text("Add")
                                        .click(function() {
                                            var host = $(this).closest('tr').children("td:eq(1)")[0].firstChild.data;
                                            $.akiyoshi.node.postModal(host);
                                        })
                                        .gat()
                                        ;
                                    };
                                    
                                })
                                .gat()
                            .gat()
                            ;
                        };
                    })
                    .gat()
                .gat()
                .tag("div", {id:"pie"}).gat()
            .gat()
            ;
            var data = [
                { label: "Series1",  data: 10},
                { label: "Series2",  data: 30},
                { label: "Series3",  data: 90},
                { label: "Series4",  data: 70},
                { label: "Series5",  data: 80},
                { label: "Series6",  data: 110}
            ];
            var options = {
                series: {
                    pie: {
                        show: true,
                    }
                }
            };
            
            //$.plot($("#pie"), data, options);
            
            if (0 < data.length) {
                $("table#servers-table").tablesorter({sortList: [[1,0]]});
            };
		});
	};

    this.graph = function(host) {
        $.akiyoshi.ajax.async({
            type: "GET",
            url: "/monitor/" + host
        })
        .success(function(data) {
            $("#main")
                .tagset("div", {class: "pills"})
                .next(function() {
                    for (var key in data) {
                        $(this).tag("li")
                            .tag("a", {href: "#graph", id: data[key].url}).text(key).click(function() {
                                $("#graph")
                                    .tagset("ul", {class: "media-grid"})
                                        .tag("li")
                                            .tag("a", {href: "#"})
                                                .tag("img", {class: "thumbnail", src: $(this).attr("id")}).gat()
                                            .gat()
                                        .gat()
                                    .gat();
                            }).gat()
                            .gat();
                    }
                })
                .gat()
                .tag("div", {class: "clear"}).gat()
                .tag("div", {id: "graph", class: "graph"}).gat()
            ;
        })
        .error(function(jqXHR, textStatus, errorThrown) {
			callback(textStatus);
		})
		.end()
		;
        
    };
});
