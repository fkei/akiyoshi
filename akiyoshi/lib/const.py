
rrd = {
    "small": {
        "font": "DEFAULT:5:",
        "width": "200",
        "height": "100",
        "comment": "color             min        max       avg        cur\\n",
        },
    "normal": {
        "font": "DEFAULT:7:",
        "width": "600",
        "height": "400",
        "comment": "color             min        max       avg        cur\\n",
        },
    "normal-wide": {
        "font": "DEFAULT:7:",
        "width": "600",
        "height": "200",
        "comment": "color             min        max       avg        cur\\n",
        },
    "large": {
        "font": "DEFAULT:14:",
        "width": "800",
        "height": "500",
        "comment": "color             min        max       avg        cur\\n",
        }
    }

format = {
    "rrd" : {
        "1hour" : "%H:%M", # 01:01
        "12hour" : "%H:%M", # 01:01
        "1day" : "%H:%M", # 01:01
        "7day" : "%m/%d", # 01/01
        "30day" : "%m/%d", # 01/01
        "365day" : "%y/%m", # 2011/01
        "default": "%y/%m/%d %H:%M" # 1011/01/01 01:01
        }
    }

system = {
    }
