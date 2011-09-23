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
                        var popup = function(data) {
                            var ret = "<b>Tag</b><br />";
                            for (var j=0; j < data.tags.length; j++) {
                                ret += "&nbsp" + data.tags[j] + "&nbsp;";
                            }
                            ret += "<br /><br /><b>NoteBook</b><br />";
                            ret += "<pre>" + data.notebook || "" + "</pre>";
                            return ret;
                        };
                        
                        for (var i = 0; i < data.length; i++) {
                            $(this)
                            .tag("tr")
                                .tag("td").text(i).gat()
                                .tag("td", {class:"host", style: "color: #00438A;"}).text(data[i].name).next(function(){
                                    $.akiyoshi.bootstrap.popovers($(this), "Infomation", popup(data[i]), {html: true});
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
                    var all = data.all;
                    var nodes = data.nodes;
                    for (var i = 0; i < all.length; i++) {
                        $(this).tag("li")
                            .tag("a", {href: "#graph", id: "/graph/" + host + "/" + all[i]}).text(all[i]).click(function() {
                                $("#graph")
                                    .tagset("ul", {class: "media-grid"})
                                        .tag("li")
                                            .tag("a", {href: "#"})
                                                .tag("img", {class: "thumbnail", src: $(this).attr("id")}).gat()
                                            .gat()
                                        .gat()
                                    .gat();
                            }).gat()
                        .gat()
                        ;
                    };
                    // Action
                    $.akiyoshi.action.update([
                        {name: "Home", link: "/"},
                        {name: "Graph - " + host}
                    ]);
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
