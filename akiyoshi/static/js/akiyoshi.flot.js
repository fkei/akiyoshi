$.akiyoshi.addHandler("flot", new function() {
	this.view = function(elem, url, data, callback) {
        if (0 < elem.find(".flot").length) {
            return; // double check
        }

        data = data || {
            resolution: 300,
            interval: "1day"
        };

        $.akiyoshi.ajax.async({
            type: "GET",
            url: url,
            data: data
        })
		.success(function(data) {
            $.akiyoshi.flot.makeFlot(elem, data, function(err, data) {
			    callback(null, data);
            });
		})
		.error(function(jqXHR, textStatus, errorThrown) {
			callback(textStatus);
		})
		.end()
		;
    };
    
    this.makeFlot = function(elem, data, callback) {
        //var idle = data.datasets["nice"]["data"];
        //var hoge = new Date();
        //for(var i =0; i< idle.length; i++) {
        //    hoge.setTime(idle[i][0]);
        //    console.log(idle[i][0]);
        //    console.log(hoge);
        //}
        /***** functions *****/
        var showTooltip = function(x, y, label, xval, yval) {
            xval = $.akiyoshi.util.date2str(xval);
            var contents = label + " : x = " + xval + ". y = " + yval;
            var tooltip = $('<div class="tooltip">' + contents + '</div>').css({
                position: 'absolute',
                display: 'none',
                top: y - 40,
                left: x - 20,
                border: '1px solid #fdd',
                padding: '2px',
                'background-color': '#fee',
                opacity: 0.80
            });
            //$.akiyoshi.bootstrap.popovers(tooltip, label, content, {html: true});
            tooltip.appendTo(elem).fadeIn(200);
            //tooltip.appendTo("body").fadeIn(200);
        };
        
        var updateLegend = function() {
            updateLegendTimeout = null;
            var pos = latestPosition;
            var axes = plot.getAxes();
            if (pos.x < axes.xaxis.min || pos.x > axes.xaxis.max ||
                pos.y < axes.yaxis.min || pos.y > axes.yaxis.max)
                return;

            var i, j, dataset = plot.getData();
            for (i = 0; i < dataset.length; ++i) {
                var series = dataset[i];
                // find the nearest points, x-wise
                for (j = 0; j < series.data.length; ++j)
                    if (series.data[j][0] > pos.x)
                        break;
                // now interpolate
                var y, p1 = series.data[j - 1], p2 = series.data[j];
                if (p1 == null)
                    y = p2[1];
                else if (p2 == null)
                    y = p1[1];
                else
                    y = p1[1] + (p2[1] - p1[1]) * (pos.x - p1[0]) / (p2[0] - p1[0]);

                elem.find(".overviewLegend td.legendLabel").eq(i)
                    .text(series.label.replace(/=.*/, "= " + y.toFixed(2)));
                //legends.find(".legendLabel").eq(i).text(series.label.replace(/=.*/, "= " + y.toFixed(2)));
            }
        };
        
        // チェック項目をグラフ描画情報に設定
        var plotAccordingToChoices = function() {
            var data = [];
            choiceContainer.find("input:checked").each(function () {
                var key = $(this).attr("name");
                if (key && datasets[key])
                    data.push(datasets[key]);
            });
            
            if (data.length > 0) {
                plot = $.plot(elem.find(".placeholder"), data, $.extend(true, {}, options));
                
                legends = elem.find(".miniature .overviewLegend");
                legends.each(function () {
                    $(this).css('width', $(this).width());
                });


                // miniture setup overview
                var ovdata = [];
                for (var key in datasets) {
                    ovdata.push(datasets[key]);
                }
                overview = $.plot(elem.find(".overview"), ovdata, {
                    legend: {
                        show: false
                    },
                    series: {
                        lines: {
                            show: true,
                            lineWidth: 1
                        },
                        shadowSize: 0
                    },
                    xaxis: {
                        ticks: 4
                    },
                    yaxis: {
                        ticks: 3
                    },
                    grid: {
                        color: "#999"
                    },
                    selection: {
                        mode: "xy"
                    }
                });
            };
        };

        /***** part(html) display *****/
        elem = $.akiyoshi.flot.makeTemplate(elem);

        /***** flot options *****/
        var options = {
            series: {
                lines: {
                    show: true
                },
                points: {
                    show: true
                } // 値のところにポイント（丸）が置かれる
            },
            legend: {
                noColumns: 2,
                show: true,
                container: elem.find(".overviewLegend")
            },
            xaxis: {
                tickDecimals: 1,
                ticks: 5, // ｙ軸の間隔
                mode: "time",
                timeformat: "%H:%M"
                //timeformat: "%y/%m/%d %H:%M"
            },
            yaxis: {
                min: 0,
                //max:100,
                ticks: 4
            },
            selection: {
                mode: "xy"
            },
            grid: {
                hoverable: true,
                clickable: true,
                autoHighlight: false
            },
            crosshair: {
                mode: "x"
            }
        };

        /***** variable *****/
        var plot = null;
        var previousPoint = null;
        var updateLegendTimeout = null;
        var latestPosition = null;
        var legends = null;
        var overview = null;

        /*****  main flow *****/
        var datasets = data["datasets"];
        var i = 0;

        // カラーリング
        $.each(datasets, function(key, val) {
            val.color = i;
            ++i;
        });
        var choiceContainer = elem.find(".flot .detail .choices");

        // 項目ON/OFF checkbox
        choiceContainer
        .tag("div", {"class": "clearfix"})
            .tag("label", {id: "optionsCheckboxes"}).text("List of options").gat()
            .tag("div", {"class":"input", style: "margin-left: 150px;"})  
                .tag("ul", {"class": "inputs-list"}).next(function() {
                    var i = 0;
                    for (var key in datasets) {
                        $(this)
                        .tag("li")
                            .tag("label")
                                .tag("input", {type: "checkbox", name: key, checked: "checked", value: "option"+i, id: "id"+key}).gat()
                                .tag("span", {style: "padding-left: 4px;"}).text(key).gat()
                            .gat()
                        .gat()
                        ;
                        i++;
                    }
                })
            .gat()
            .gat()
        .gat()
        ;

        // 項目checkboxをクリックするとグラフを再描画
        choiceContainer.find("input").click(plotAccordingToChoices);
        
        elem.find(".placeholder").bind("plothover", function (event, pos, item) {

            // Show mouse position
            if (elem.find(".enablePosition:checked").length > 0) { 
                var xval = $.akiyoshi.util.date2str(pos.x.toFixed(2));
                var str = "x = " + xval + ", y = " + pos.y.toFixed(2);
                elem.find(".hoverdata").attr("value", str);
            }
            
            if (elem.find(".enableTooltip:checked").length > 0) {
                if (item) {
                    if (previousPoint != item.dataIndex) {
                        previousPoint = item.dataIndex;
                        elem.find(".tooltip").remove();
                        var x = item.datapoint[0].toFixed(2),
                        y = item.datapoint[1].toFixed(2);

                        var _label = item.series.label.replace(" = 0", "");
                        showTooltip(item.pageX, item.pageY,
                                    _label, x, y);
                    }
                }
                else {
                    elem.find(".tooltip").remove();
                    previousPoint = null;
                }
            }

            latestPosition = pos;
            if (!updateLegendTimeout)
                updateLegendTimeout = setTimeout(updateLegend, 50);
        });

    
        elem.find(".placeholder").bind("plotselected", function (event, ranges) {
            if (ranges.xaxis.to - ranges.xaxis.from < 0.00001)
                ranges.xaxis.to = ranges.xaxis.from + 0.00001;
            if (ranges.yaxis.to - ranges.yaxis.from < 0.00001)
                ranges.yaxis.to = ranges.yaxis.from + 0.00001;
                
            plot = $.plot(elem.find(".placeholder"), plot.getData(ranges.xaxis.from, ranges.xaxis.to),
                          $.extend(true, {}, options, {
                              xaxis: { min: ranges.xaxis.from, max: ranges.xaxis.to },
                              yaxis: { min: ranges.yaxis.from, max: ranges.yaxis.to }
                          }));
        
            overview.setSelection(ranges, true);
        });

        
        elem.find(".overview").bind("plotselected", function (event, ranges) {
            plot.setSelection(ranges);
        });

        // 描画する
        plotAccordingToChoices();
    };
    
    this.makeTemplate = function(elem) {
        elem
        .tagset("div", {"class": "flot"})
            .tag("div", {style: "float:left;"})
                .tag("div", {"class": "placeholder", style: "width:400px;height:200px"}).gat()
            .gat()

            .tag("div", {"class": "miniture", style: "float:left;"})
                .tag("div", {"class": "overview", style: "width:266px;height:100px"}).gat()
                .tag("p", {"class": "overviewLegend", style: "margin-left:10px;"}).gat()
            .gat()

            .tag("div", {"class": "clear"}).gat()

            .tag("span", {"class": "label cursor notice", style:"margin-left: 54px"}).text("Detail").click(function() {
                $(this).parent().find(".detail").toggle("fast");
            }).gat()

            .tag("div", {"class": "detail", style: "display:none;"})
                .tag("div", {"class": "choices"}).gat()
                .tag("div", {"class": "clearfix", id: "clickdata"})
                    .tag("label", {for: "prependedInput2"}).text("Show mouse position").gat()
                    .tag("div", {"class": "input"})
                        .tag("div", {"class": "input-prepend"})
                            .tag("label", {"class": "add-on"})
                                .tag("input", {type: "checkbox", name: "enablePosition", "class": "enablePosition", checked: "checked"}).gat()
                            .gat()
                            .tag("input", {style: "font-weight:bold", "class": "large hoverdata", name: "hoverdata", size: "32", type: "text"}).gat()
                        .gat()
                    .gat()
                .gat()

                .tag("div", {"class": "clearfix"})
                    .tag("label", {id: "optionsCheckboxes"}).text("Enable tooltip").gat()
                    .tag("div", {"class": "input"})
                        .tag("ul", {"class": "inputs-list"})
                            .tag("li")
                                .tag("label")
                                    .tag("input", {type: "checkbox", name: "enableTooltip", "class": "enableTooltip", checked: "checked"}).gat()
                                .gat()    
                            .gat()    
                        .gat()       
                    .gat()    
                .gat()    
            .gat()    
        .gat()    
        ;
        return elem;
    };
});

