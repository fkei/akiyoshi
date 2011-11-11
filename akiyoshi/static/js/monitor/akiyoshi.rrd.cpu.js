function getRrdCpu(id, core) {
    var types = ['idle', 'nice', 'steal', 'user', 'interrupt', 'softirq', 'system', 'wait'];
    var rrds = [];

    var graphOpts = {
        legend: {
            position: "nw",
            noColumns: 8
        },
        lines: {
             show:true
        },
        yaxis: {
             autoscaleMargin: 0.20
        }
    };
    
    var dsGraphOpts = {
        'DERIVE': {
            title: "タイトル",
            checked: true,
            label: "ラベル",
            color: "#ff8000", 
            lines: {
                show: true,
                fill: true,
                fillColor:"#ffff80"
            },
            yaxis: 1,
            stack: "positive"
        }
    };

    var rrdflot_defaults = {
        legend: "BottomRight",
        num_cb_rows: 24,
        use_elem_buttons: true,
        multi_ds: true,
        multi_rra: true,
        use_checked_DSs: true,
        checked_DSs: [],
        use_rra: true,
        rra: 1,
        use_windows: true,
        window_min: 0,
        window_max: 0,
        graph_height: "200px",
        graph_width: "400px",
        scale_height: "100px",
        scale_width: "200px",
        timezone: 9
    };

    var make = function() {
        if (rrds.length == types.length) {
            var sum = new RRDFileSum(rrds);
            var flot = new rrdFlot(id, sum, graphOpts, dsGraphOpts, rrdflot_defaults);
        }
    };

    var url = '/rrd/cpu/' + core;
    for (var i=0; i < types.length; i++) {
        FetchBinaryURLAsync(url + '/' + types[i], function(buffer) {
            var rrd = undefined;
            try {
                rrd = new RRDFile(buffer);
            } catch (x) {
                alert('new RRDFile error!!');
            }
            if (rrd) {
                rrds.push(rrd);
                make();
            }
        });
    };
};

function getRrdCpuMatrix(id, core) {
    var types = ['idle', 'nice', 'steal', 'user', 'interrupt', 'softirq', 'system', 'wait'];

    var graphOpts = {
        legend: {
            position: "nw",
            noColumns: 3
        },
        lines: {
             show:true
        },
        yaxis: {
             autoscaleMargin: 0.02
        }
    };
    
    var dsGraphOpts = {
        'idle': {
            title: "あいどる",
            checked: false,
            label: "アイドル",
            //color: "#ff8000", 
            lines: {
                show: true,
                //fill: true,
                //fillColor:"#ffff80"
            },
            //yaxis: 1,
            //stack: "positive"
        },
        'nice': {
            title: "ないす",
            checked: true,
            label: "ナイス",
            //color: "#ff8000", 
            lines: {
                show: true,
                //fill: true,
                //fillColor:"#ffff80"
            },
            //yaxis: 1,
            //stack: "positive"
        },
        'steal': {
            title: "steal",
            checked: true,
            label: "steal",
            //color: "#ff8000", 
            lines: {
                show: true,
                //fill: true,
                //fillColor:"#ffff80"
            },
            //yaxis: 1,
            //stack: "positive"
        },
        'user': {
            title: "ゆーざー",
            checked: true,
            label: "ユーザ",
            //color: "#ff8000", 
            lines: {
                show: true,
                //fill: true,
                //fillColor:"#ffff80"
            },
            //yaxis: 1,
            //stack: "positive"
        },
        'interrupt': {
            title: "わりこみ",
            checked: true,
            label: "割り込み",
            //color: "#ff8000", 
            lines: {
                show: true,
                //fill: true,
                //fillColor:"#ffff80"
            },
            //yaxis: 1,
            //stack: "positive"
        },
        'softirq': {
            title: "そふとIRQ",
            checked: true,
            label: "ソフトIRQ",
            //color: "#ff8000", 
            lines: {
                show: true,
                //fill: true,
                //fillColor:"#ffff80"
            },
            //yaxis: 1,
            //stack: "positive"
        },
        'system': {
            title: "しすてむ",
            checked: true,
            label: "システム",
            //color: "#ff8000", 
            lines: {
                show: true,
                //fill: true,
                //fillColor:"#ffff80"
            },
            //yaxis: 1,
            //stack: "positive"
        },
        'wait': {
            title: "たいき",
            checked: true,
            label: "待機",
            //color: "#ff8000", 
            lines: {
                show: true,
                //fill: true,
                //fillColor:"#ffff80"
            },
            //yaxis: 1,
            //stack: "positive"
        },
        
    };

    var rrdflot_defaults = {
        //legend: "BottomRight",
        //num_cb_rows: 2,
        //use_elem_buttons: true,
        multi_ds: true,
        multi_rra: true,
        use_checked_DSs: true,
        checked_DSs: [],
        use_rra: true,
        rra: 1,
        use_windows: true,
        //window_min: 0,
        //window_max: 0,
        //graph_height: "200px",
        //graph_width: "400px",
        //scale_height: "100px",
        //scale_width: "200px",
        //timezone: 9
    };

    var make = function() {
        if (rrds.length == types.length) {
            var flot = new rrdFlotMatrix(id, rrds, null, graphOpts, dsGraphOpts, rrdflot_defaults);
        }
    };

    var rrds = [];
    var url = '/rrd/cpu/' + core;
    for (var i = 0; i < types.length; i++) {
        FetchBinaryURLAsync(url + '/' + types[i], function(buffer, type) {
            var rrd = undefined;
            try {
                rrd = new RRDFile(buffer);
            } catch (x) {
                alert('new RRDFile error!!');
            }
            if (rrd) {
                rrds.push([type, rrd]);
                make();
            }
        }, types[i]);
    };
};
