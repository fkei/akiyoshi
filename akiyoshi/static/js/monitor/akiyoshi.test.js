$.akiyoshi.addHandler("test", new function() {

    this.init = function() {
    };

    this.flot = function(id) {
        /***** データ情報 *****/
        var datasets = {
            "usa": {
                label: "USA = 0",
                data: [[1988, 483994], [1989, 479060], [1990, 457648], [1991, 401949], [1992, 424705], [1993, 402375], [1994, 377867], [1995, 357382], [1996, 337946], [1997, 336185], [1998, 328611], [1999, 329421], [2000, 342172], [2001, 344932], [2002, 387303], [2003, 440813], [2004, 480451], [2005, 504638], [2006, 528692]]
                //data: [[483994], [479060], [457648], [401949], [424705], [402375], [377867], [357382], [337946], [336185], [328611], [329421], [342172], [344932], [387303], [440813], [480451], [504638], [528692]]
            },
            "russia": {
                label: "Russia = 0",
                data: [[1988, 218000], [1989, 203000], [1990, 171000], [1992, 42500], [1993, 37600], [1994, 36600], [1995, 21700], [1996, 19200], [1997, 21300], [1998, 13600], [1999, 14000], [2000, 19100], [2001, 21300], [2002, 23600], [2003, 25100], [2004, 26100], [2005, 31100], [2006, 34700]]
            },
            "uk": {
                label: "UK = 0",
                data: [[1988, 62982], [1989, 62027], [1990, 60696], [1991, 62348], [1992, 58560], [1993, 56393], [1994, 54579], [1995, 50818], [1996, 50554], [1997, 48276], [1998, 47691], [1999, 47529], [2000, 47778], [2001, 48760], [2002, 50949], [2003, 57452], [2004, 60234], [2005, 60076], [2006, 59213]]
            },
            "germany": {
                label: "Germany = 0",
                data: [[1988, 55627], [1989, 55475], [1990, 58464], [1991, 55134], [1992, 52436], [1993, 47139], [1994, 43962], [1995, 43238], [1996, 42395], [1997, 40854], [1998, 40993], [1999, 41822], [2000, 41147], [2001, 40474], [2002, 40604], [2003, 40044], [2004, 38816], [2005, 38060], [2006, 36984]]
            },
            "denmark": {
                label: "Denmark = 0",
                data: [[1988, 3813], [1989, 3719], [1990, 3722], [1991, 3789], [1992, 3720], [1993, 3730], [1994, 3636], [1995, 3598], [1996, 3610], [1997, 3655], [1998, 3695], [1999, 3673], [2000, 3553], [2001, 3774], [2002, 3728], [2003, 3618], [2004, 3638], [2005, 3467], [2006, 3770]]
            },
            "sweden": {
                label: "Sweden = 0",
                data: [[1988, 6402], [1989, 6474], [1990, 6605], [1991, 6209], [1992, 6035], [1993, 6020], [1994, 6000], [1995, 6018], [1996, 3958], [1997, 5780], [1998, 5954], [1999, 6178], [2000, 6411], [2001, 5993], [2002, 5833], [2003, 5791], [2004, 5450], [2005, 5521], [2006, 5271]]
            },
            "norway": {
                label: "Norway = 0",
                data: [[1988, 4382], [1989, 4498], [1990, 4535], [1991, 4398], [1992, 4766], [1993, 4441], [1994, 4670], [1995, 4217], [1996, 4275], [1997, 4203], [1998, 4482], [1999, 4506], [2000, 4358], [2001, 4385], [2002, 5269], [2003, 5066], [2004, 5194], [2005, 4887], [2006, 4891]]
            }
        };

        /***** オプション情報 *****/
        var options = {
            series: {
                lines: {show: true},
                points: {show: true} // 値のところにポイント（丸）が置かれる
            },
            legend: {
                noColumns: 1,
                show: true,
                container: $("#overviewLegend")
            },
            xaxis: {
                tickDecimals: 0,
                ticks: 5 // ｙ軸の間隔
            },
            yaxis: {
                min: 0,
                ticks: 1
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

        /***** 関数 *****/        
        function showTooltip(x, y, contents) {
            $('<div id="tooltip">' + contents + '</div>').css( {
                position: 'absolute',
                display: 'none',
                top: y + 5,
                left: x + 5,
                border: '1px solid #fdd',
                padding: '2px',
                'background-color': '#fee',
                opacity: 0.80
            }).appendTo("body").fadeIn(200);
        };
        
        function updateLegend() {
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

                //legends.eq(i).text(series.label.replace(/=.*/, "= " + y.toFixed(2)));
                legends.find(".legendLabel").eq(i).text(series.label.replace(/=.*/, "= " + y.toFixed(2)));
                
            }
        };
        
        // チェック項目をグラフ描画情報に設定
        function plotAccordingToChoices() {
            var data = [];
            choiceContainer.find("input:checked").each(function () {
                var key = $(this).attr("name");
                if (key && datasets[key])
                    data.push(datasets[key]);
            });
            
            if (data.length > 0) {
                plot = $.plot($("#placeholder"), data, $.extend(true, {}, options));

                //legends = $("#placeholder .legendLabel");
                legends = $("#miniature #overviewLegend");
                legends.each(function () {
                    $(this).css('width', $(this).width());
                });


                // miniture setup overview
                var ovdata = [];
                for (var key in datasets) {
                    ovdata.push(datasets[key]);
                }
                overview = $.plot($("#overview"), ovdata, {
                    legend: {
                        show: false,
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
                        ticks: 3,
                    },
                    grid: {
                        color: "#999"
                    },
                    selection: {
                        mode: "xy"
                    }
                });
            }
        }

        /***** メンバ変数 *****/
        var plot = null;
        var previousPoint = null;
        var updateLegendTimeout = null;
        var latestPosition = null;
        var legends = null;
        var overview = null;

        /***** メイン処理 *****/
        var i = 0;

        // カラーリング
        $.each(datasets, function(key, val) {
            val.color = i;
            ++i;
        });

        var choiceContainer = $("#choices"); // 項目ON/OFF
        // 項目checkboxの表示
        choiceContainer
        .tagset("div", {class: "clearfix"})
            .tag("label", {id: "optionsCheckboxes"}).text("List of options").gat()
                .tag("div", {class:"input", style: "margin-left: 150px;"})  
                    .tag("ul", {class: "inputs-list"}).next(function() {
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
        .gat()
        ;

        // 項目checkboxをクリックするとグラフを再描画
        choiceContainer.find("input").click(plotAccordingToChoices);
        
        $("#placeholder").bind("plothover", function (event, pos, item) {

            // Show mouse position
            if ($("#enablePosition:checked").length > 0) {
                var str = "(" + pos.x.toFixed(2) + ", " + pos.y.toFixed(2) + ")";
                $("#hoverdata").attr("value", str);
            }
            
            if ($("#enableTooltip:checked").length > 0) {
                if (item) {
                    if (previousPoint != item.dataIndex) {
                        previousPoint = item.dataIndex;
                        
                        $("#tooltip").remove();
                        var x = item.datapoint[0].toFixed(2),
                        y = item.datapoint[1].toFixed(2);
                        
                        showTooltip(item.pageX, item.pageY,
                                    item.series.label + " of " + x + " = " + y);
                    }
                }
                else {
                    $("#tooltip").remove();
                    previousPoint = null;
                }
            }

            latestPosition = pos;
            if (!updateLegendTimeout)
                updateLegendTimeout = setTimeout(updateLegend, 50);
        });

    
        $("#placeholder").bind("plotselected", function (event, ranges) {
            if (ranges.xaxis.to - ranges.xaxis.from < 0.00001)
                ranges.xaxis.to = ranges.xaxis.from + 0.00001;
            if (ranges.yaxis.to - ranges.yaxis.from < 0.00001)
                ranges.yaxis.to = ranges.yaxis.from + 0.00001;
                
            plot = $.plot($("#placeholder"), plot.getData(ranges.xaxis.from, ranges.xaxis.to),
                          $.extend(true, {}, options, {
                              xaxis: { min: ranges.xaxis.from, max: ranges.xaxis.to },
                              yaxis: { min: ranges.yaxis.from, max: ranges.yaxis.to }
                          }));
        
            overview.setSelection(ranges, true);
        });
        $("#overview").bind("plotselected", function (event, ranges) {
            plot.setSelection(ranges);
        });

        // 描画する
        plotAccordingToChoices();
    };
});
