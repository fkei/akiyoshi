#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import rrdtool

from lib.const import rrd
from lib.common import generate_phrase

def make(read_dir, write_dir, category, start, end, size="small"):
    if size:
        options = rrd[size]
    else:
        options = rrd["small"]

    if os.path.isdir(read_dir) is False:
        print "read_dir error" # TODO
    if os.path.isfile("/tmp/hoge.png") is False:
        print "write_dir error" # TODO

    write_file_path = "%s/%s.png" % (write_dir, generate_phrase(12))

    rrdtool.graph(write_file_path,
        "--font", options["font"],
        "--title", str(category),
        "--vertical-label", "jiffies",
        "--upper-limit", "100",
        "--rigid",
        "--width", options["width"],
        "--height", options["height"],
        "--start", start,
        "--end",   end,
        "--legend-direction", "bottomup",
        "DEF:idle=%s/cpu-idle.rrd:value:AVERAGE" % str(read_dir),
        "DEF:interrupt=%s/cpu-interrupt.rrd:value:AVERAGE" % str(read_dir),
        "DEF:nice=%s/cpu-nice.rrd:value:AVERAGE" % str(read_dir),
        "DEF:user=%s/cpu-user.rrd:value:AVERAGE" % str(read_dir),
        "DEF:wait=%s/cpu-wait.rrd:value:AVERAGE" % str(read_dir),
        "DEF:system=%s/cpu-system.rrd:value:AVERAGE" % str(read_dir),
        "DEF:softirq=%s/cpu-softirq.rrd:value:AVERAGE" % str(read_dir),
        "DEF:steal=%s/cpu-steal.rrd:value:AVERAGE" % str(read_dir),
        "AREA:steal#000000:Steal    ",
        "GPRINT:steal:MIN:%8.2lf",
        "GPRINT:steal:MAX:%8.2lf",
        "GPRINT:steal:AVERAGE:%8.2lf",
        "GPRINT:steal:LAST:%8.2lf\\n",
        "STACK:interrupt#FF00FF:Interrupt",
        "GPRINT:interrupt:MIN:%8.2lf",
        "GPRINT:interrupt:MAX:%8.2lf",
        "GPRINT:interrupt:AVERAGE:%8.2lf",
        "GPRINT:interrupt:LAST:%8.2lf\\n",
        "STACK:softirq#FF22DD:SoftIRQ  ",
        "GPRINT:softirq:MIN:%8.2lf",
        "GPRINT:softirq:MAX:%8.2lf",
        "GPRINT:softirq:AVERAGE:%8.2lf",
        "GPRINT:softirq:LAST:%8.2lf\\n",
        "STACK:system#FF0000:System   ",
        "GPRINT:system:MIN:%8.2lf",
        "GPRINT:system:MAX:%8.2lf",
        "GPRINT:system:AVERAGE:%8.2lf",
        "GPRINT:system:LAST:%8.2lf\\n",
        "STACK:wait#FFDD00:Wait     ",
        "GPRINT:wait:MIN:%8.2lf",
        "GPRINT:wait:MAX:%8.2lf",
        "GPRINT:wait:AVERAGE:%8.2lf",
        "GPRINT:wait:LAST:%8.2lf\\n",
        "STACK:user#0000FF:User     ",
        "GPRINT:user:MIN:%8.2lf",
        "GPRINT:user:MAX:%8.2lf",
        "GPRINT:user:AVERAGE:%8.2lf",
        "GPRINT:user:LAST:%8.2lf\\n",
        "STACK:nice#00FF00:Nice     ",
        "GPRINT:nice:MIN:%8.2lf",
        "GPRINT:nice:MAX:%8.2lf",
        "GPRINT:nice:AVERAGE:%8.2lf",
        "GPRINT:nice:LAST:%8.2lf\\n",
        "STACK:idle#EEEEEE:Idle     ",
        "GPRINT:idle:MIN:%8.2lf",
        "GPRINT:idle:MAX:%8.2lf",
        "GPRINT:idle:AVERAGE:%8.2lf",
        "GPRINT:idle:LAST:%8.2lf\\n",
        "COMMENT:%s" % options["comment"],
        "COMMENT: \\n"
    )
    return write_file_path

if __name__ == '__main__':
    _start_year = 2011
    _start_month = 9
    _start_day = 5
    _start_hour = 18
    _start_minute = 0
    _start_second = 0

    _end_year = 2011
    _end_month = 9
    _end_day = 6
    _end_hour = 10
    _end_minute = 0
    _end_second = 0

    import time
    import datetime
    def create_epochsec(year, month, day, hour, minute, second):
        return str(int(time.mktime(datetime.datetime(year, month, day, hour, minute, second).timetuple())))

    start = create_epochsec(_start_year, _start_month, _start_day, _start_hour, _start_minute, _start_second)
    end = create_epochsec(_end_year, _end_month, _end_day, _end_hour, _end_minute, _end_second)

    make("/var/lib/collectd/xxx/cpu-0",
         "/tmp/hoge.gif",
         start,
         end,
         "large")
