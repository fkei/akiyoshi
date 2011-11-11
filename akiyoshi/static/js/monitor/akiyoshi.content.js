$.akiyoshi.addHandler("content", new function() {
	this.info = function(id, category, param) {

		$.akiyoshi.node.info(category, function(err, data) {
			if (err) {
				return alert("TODO err");
			}
            $("#"+id)
            .empty()
            .next(function() {
                if (category) {
                    $(this)
                    .tag("div", {"class":"well", style:"padding: 14px 19px;"}).next(function() {
                        var elem = this;
                        $.akiyoshi.monitor.info(category, param, function(err, result) {
                            for (var i =0; i< result.all.length; i++) {
                                $(elem).tag("span", {style:"margin-left: 5px;",
                                                     "class": "btn cursor",
                                                     "group": result.all[i]}).text(result.all[i]).click(function() {
                                    //$.akiyoshi.content.graphPills(category, $(this).attr("group"));
                                    $.akiyoshi.content.graphPills(category, {type: "tag"});
                                }).gat();
                            }
                        });
                    })
                    .gat()
                    ;
                }
            })
            .tag("div", {"class":"well", style:"padding: 14px 19px;"})
                .tag("span", {style:"margin-left: 5px;",
                              "class": "btn cursor", "group": "compare"}).text("Group View").click(function() {
                    var hosts = [];
                    $("#servers-table tbody tr").each(function(idx, elem) {
                        if($(this).children("td:eq(3)").children("input:checkbox").is(':checked') === true) {
                            hosts.push($(this).children("td:eq(1)").attr("data-host"));
                        }
                    });
                    $.akiyoshi.content.graphPills(hosts.join(","), {type: "group"});
                }).gat()
                .tag("span", {style:"margin-left: 5px;",
                              "class": "btn cursor", "group": "compare"}).text("Compare View").click(function() {
                    var hosts = [];
                    $("#servers-table tbody tr").each(function(idx, elem) {
                        if($(this).children("td:eq(3)").children("input:checkbox").is(':checked') === true) {
                            hosts.push($(this).children("td:eq(1)").attr("data-host"));
                        }
                    });
                    $.akiyoshi.content.graphPills(hosts.join(","), {type: "compare"});
                }).gat()
            .gat()
            .tag("table", {"class": "zebra-striped", id: "servers-table"})
                .tag("thead")
                    .tag("tr")
                        .tag("th", {"class": "header"}).text("#").gat()
                        .tag("th", {"class": "yellow header headerSortDown"}).text("Host").gat()
                        .tag("th", {"class": "blue header headerSortDown"}).text("Status").gat()
                        .tag("th", {"class": "purple header headerSortDown"}).text("Select").gat()
                        .tag("th", {"class": "green header headerSortDown"}).text("Action").gat()
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
                                .tag("td", {"class":"host", style: "color: #00438A;", "data-host": data[i].name}).text(data[i].name).next(function(){
                                    $.akiyoshi.bootstrap.popovers($(this), "Infomation", popup(data[i]), {html: true});
                                })
                                .gat()
                                .tag("td").text(data[i].control ? "Managed" : "Unmanaged").gat()
                                .tag("td", {width: "70px", style: "text-align: center;"})
                                    .tag("input", {"type": "checkbox", id: "select-" + data[i].name, name: "select-" + data[i].name, value: data[i].name, checked: "checked"}).gat()
                                .gat()
                                .tag("td").next(function() {
                                    $(this)
                                    .tag("span", {"class": "label cursor"}).click(function() {
                                        //var host = $(this).closest('tr').children("td:eq(1)")[0].firstChild.data;
                                        var host = $(this).closest('tr').children("td:eq(1)").attr("data-host");
                                        $.akiyoshi.content.graphPills(host, {type: "host"});
                                    }).text("Graph").gat();

                                    if (data[i].control === false) {
                                        // Unmanaged
                                        $(this)
                                        .tag("span", {"class": "label cursor", "data-controls-modal": "modal", "data-backdrop": true, "data-keyboard": true}).text("Add")
                                        .click(function() {
                                            var host = $(this).closest('tr').children("td:eq(1)")[0].firstChild.data;
                                            $.akiyoshi.node.postModal(host, function(err, result) {
                                                $.akiyoshi.content.info(id, category); // content reload
                                            });
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
            if (0 < data.length) {
                $("table#servers-table").tablesorter({sortList: [[1,0]]});
            };
		});
	};

    this.__graphLinks = function(id, link, extension, param, callback) {
        var self = this;
        console.log(link);
        if (!param.interval) {
            $("#"+id+" .well").children("span").each(function(idx, elem) {
                if ($(this).is(".primary")) {
                    param.interval = $(this).attr("id").replace(/^graph/, "");
                }
            });
        }

        var reload = function(param) {
            self.__graphLinks(id, link, extension, param, callback);
        };

        var makeRrdTemplate = function(err, elem, link) {
            if (err) {
                alert("TODO : error ");
                return false;
            }
            var view = elem.find(".view");
            if (view) {
                view.remove();
            }

            elem
            .tag("div", {"class": "view"})
                .tag("ul", {"class": "media-grid"})
                    .tag("li")
                        .tag("a", {})
                            .tag("img", {"class": "thumbnail", src: link.url + extension + '?interval=' + param.interval + "&type=" + param.type}).gat()
                        .gat()
                    .gat()
                    .gat()
                    .tag("span", {"class": "label cursor notice", style:"margin-left: 54px"}).text("Detail").click(function() {
                        $(this).parent().find(".detail").toggle("fast");
                    }).gat()
                    .tag("div", {"class": "detail", style: "display:none;"})
                        .tag("div", {"class": "choices"})
                            .tag("div", {"class": "clearfix"})
                                .tag("label", {"class": "cboxtype"}).text("Display list").gat()
                                .tag("div", {"class": "input", style: "margin-left: 150px"})
                                    .tag("ul", {"class": "inputs-list"})
                                    .next(function() {
                                        var types = link.type;
                                        for (var k = 0; k < types.length; k++) {
                                            var type = types[k];
                                            $(this)
                                            .tag("li")
                                                .tag("label")
                                                    .tag("input", {type: "checkbox", id:type, name: type, checked:"checked",
                                                                   value: type, link: link.url, parent: link.name}).click(function() {
                                                        // Custom RRD
                                                        var nowTypes = [];
                                                        $(this).closest(".choices").find("input:checked").each(function(idx, elem) {
                                                            nowTypes.push($(this).attr("value"));
                                                        });
                                                        if (nowTypes.length < 1) {
                                                            alert("TODO not checked");
                                                            return false;
                                                        }
                                                        var link = $(this).attr("link");
                                                        var url =  link + extension + '?interval=' + param.interval + "&types=" + nowTypes.join(",") + "&type=" + param.type;
                                                        var elem = $("#"+$(this).attr("parent"));
                                                        var img = elem.find("img:.thumbnail");
                                                        img.attr("src", url);
                                                        ;
                                                    })
                                                .gat()
                                                .tag("span", {sytle: "padding-left: 4px;"}).text(type).gat()
                                            .gat()
                                        .gat()
                                        ;
                                        }
                                    })
                                .gat()
                            .gat()
                        .gat()
                    .gat()
                .gat()
            .gat()
            ;
        }

        var fn = function(err, result) {
            $("#"+id)
            .tagset("div", {"class": "well", style: "padding: 5px;"})
                .tag("span", {id: "graph1hour", style:"margin-left: 5px;", "class": "btn cursor"}).text("1 Hour").click(function() {
                    reload("1hour");
                }).gat()
                .tag("span", {id: "graph12hour", style:"margin-left: 5px;", "class": "btn cursor"}).text("12 Hour").click(function() {
                    reload("12hour");
                }).gat()
                .tag("span", {id: "graph1day", style:"margin-left: 5px;", "class": "btn cursor primary"}).text("1 Day").click(function() {
                    reload("1day");
                }).gat()
                .tag("span", {id: "graph7day", style:"margin-left: 5px;", "class": "btn cursor"}).text("1 Week").click(function() {
                    reload("7day");
                }).gat()
                .tag("span", {id: "graph30day", style:"margin-left: 5px;", "class": "btn cursor"}).text("1 Month").click(function() {
                    reload("30day");
                }).gat()
                .tag("span", {id: "graph365day", style:"margin-left: 5px;", "class": "btn cursor"}).text("1 Year").click(function() {
                    reload("365day");
                }).gat()
            .gat()
            .next(function() {
                for (var i = 0; i < result.length; i++) {
                    var data = result[i];
                    for (var j = 0; j < data.links.length; j++) {
                        $(this)
                        .tag("div", {id: data.links[j].name, uri:data.links[j].url, style:"margin: 0px 0px 34px 0px"})
                            .tag("h4").text(data.name + " - " + data.links[j].name)
                                .tag("span", {style:"margin-left: 5px;", "class": "label cursor"}).text("Flot").click(function() {
                                    $(this).parent().children().each(function(idx, elem) {
                                        $(this).removeClass("notice");
                                    });
                                    $(this).addClass("notice");

                                    var parent = $(this).closest("div");
                                    var url = parent.attr("uri") + ".dat";
                                    var elem = parent.find("div.view");
                                    $.akiyoshi.flot.view(elem, url, {interval: param.interval, type: param.type}, function() {});
                                }).gat()
                                .tag("span", {style:"margin-left: 5px;", "class": "label cursor notice"}).text("Image").click(function() {
                                    $(this).parent().children().each(function(idx, elem) {
                                        $(this).removeClass("notice");
                                    });
                                    $(this).addClass("notice");

                                    var parent = $(this).closest("div");
                                    $.akiyoshi.ajax.async({
                                        type: "GET",
                                        url: parent.attr("uri"),
                                        data: {interval: param.interval, type: param.type}
                                    })
                                    .success(function(result) {
                                        makeRrdTemplate(null, parent, data.links[0]);
                                    })
                                    .error(function(jqXHR, textStatus, errorThrown) {
			                            makeRrdTemplate(textStatus);
                                    })
                                    .end()
		                            ;
                                    //makeRrdTemplate($(this), data.links[j]);
                                }).gat()
                            .gat()
                            .next(function() { 
                               makeRrdTemplate(null, $(this), data.links[j]);
                            })
                        .gat()
                    .gat()
                        ;
                    }
                };
            });

            // select datetime.
            $("#"+id).find(".well").children().each(function(idx, elem) {
                if ($(this).attr("id") === "graph" + param.interval) {
                    $(this).addClass("primary");
                } else {
                    $(this).removeClass("primary");
                }                
            });

            if (callback) {
                callback(null);
            }
        };
        
        $.akiyoshi.ajax.async({
            type: "GET",
            url: link,
            data: param
        })
        .success(function(result) {
            fn(null, result);
        })
        .error(function(jqXHR, textStatus, errorThrown) {
			fn(textStatus);
		})
        .end()
		;
    };
    
    this.graphPills = function(host, param) {
        $.akiyoshi.monitor.info(host, param, function(err, data) {
            if (err) {
                alert("TODO: error");
                return false;
            }
            $("#main")
                .tagset("div", {"class": "pills"})
                .next(function() {
                    var all = data.all;
                    var nodes = data.nodes;
                    for (var i = 0; i < all.length; i++) {
                        $(this).tag("li")
                            .tag("a", {id: "/graph/" + host + "/" + all[i], "class":"cursor"})
                            .text(all[i]).click(function() {
                                param["interval"] = "1day";
                                $.akiyoshi.content.__graphLinks("graph", $(this).attr("id"), ".png", param);
                            }).gat()
                        .gat()
                        ;
                    };

                    // Action
                    $.akiyoshi.action.update([
                        {name: "Monitor", link: "/monitor"},
                        {name: "Graph - " + host}
                    ]);
                })
                .gat()
                .tag("div", {"class": "clear"}).gat()
                .tag("div", {id: "graph", "class": "graph"}).gat()
            ;
        });
    };
});
