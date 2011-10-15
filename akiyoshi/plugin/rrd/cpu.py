#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import rrdtool

from lib.const import rrd as RRD
from lib.common import generate_phrase
import akiyoshi


TYPE = "cpu"
DEFAULT_TYPES = ["idle", "interrupt", "nice", "user", "wait", "system", "softirq", "steal"]

def make_idle(read_dir, last=False):
    # getattr(akiyoshi.plugins["rrd"]["cpu"], "makeIdle")
    _def = [
        "DEF:idle=%s/cpu-idle.rrd:value:AVERAGE" % read_dir,
        ]

    _val = [
        "GPRINT:idle:MIN:%8.2lf",
        "GPRINT:idle:MAX:%8.2lf",
        "GPRINT:idle:AVERAGE:%8.2lf",
        "GPRINT:idle:LAST:%8.2lf\\n",
        ]

    _area = []
    if last is True:
        _area = [
            "AREA:idle#FFFFFF:Idle",
            ]
    if last is False:
        _val = ["STACK:idle#FFFFFF:Idle     "] + _val

    return (_def, _val, _area)

def make_interrupt(read_dir, last=False):
    _def = [
        "DEF:interrupt=%s/cpu-interrupt.rrd:value:AVERAGE" % read_dir,
        ]

    _val = [
        #"STACK:interrupt#EB6100:Interrupt",
        "GPRINT:interrupt:MIN:%8.2lf",
        "GPRINT:interrupt:MAX:%8.2lf",
        "GPRINT:interrupt:AVERAGE:%8.2lf",
        "GPRINT:interrupt:LAST:%8.2lf\\n",
        ]

    _area = []
    if last is True:
        _area = [
            "AREA:interrupt#EB6100:Interrupt",
            ]
    if last is False:
        _val = ["STACK:interrupt#EB6100:Interrupt"] + _val

    return (_def, _val, _area)

def make_nice(read_dir, last=False):
    _def = [
        "DEF:nice=%s/cpu-nice.rrd:value:AVERAGE" % read_dir,
        ]

    _val = [
        "GPRINT:nice:MIN:%8.2lf",
        "GPRINT:nice:MAX:%8.2lf",
        "GPRINT:nice:AVERAGE:%8.2lf",
        "GPRINT:nice:LAST:%8.2lf\\n",
        ]

    _area = []
    if last is True:
        _area = [
            "AREA:nice#FCC800:Nice     ",
            ]
    if last is False:
        _val = ["STACK:nice#FCC800:Nice     "] + _val

    return (_def, _val, _area)

def make_user(read_dir, last=False):
    _def = [
        "DEF:user=%s/cpu-user.rrd:value:AVERAGE" % read_dir,
        ]

    _val = [
        "GPRINT:user:MIN:%8.2lf",
        "GPRINT:user:MAX:%8.2lf",
        "GPRINT:user:AVERAGE:%8.2lf",
        "GPRINT:user:LAST:%8.2lf\\n",
        ]

    _area = []
    if last is True:
        _area = [
            "AREA:user#0086D1:User     ",
            ]
    if last is False:
        _val = ["STACK:user#0086D1:User     "] + _val

    return (_def, _val, _area)

def make_wait(read_dir, last=False):

    _def = [
        "DEF:wait=%s/cpu-wait.rrd:value:AVERAGE" % read_dir,
        ]

    _val = [
            "GPRINT:wait:MIN:%8.2lf",
            "GPRINT:wait:MAX:%8.2lf",
            "GPRINT:wait:AVERAGE:%8.2lf",
            "GPRINT:wait:LAST:%8.2lf\\n",
        ]

    _area = []
    if last is True:
        _area = [
            "AREA:wait#009B6B:Wait     ",
            ]
    if last is False:
        _val = ["STACK:wait#009B6B:Wait     "] + _val

    return (_def, _val, _area)

def make_system(read_dir, last=False):

    _def = [
        "DEF:system=%s/cpu-system.rrd:value:AVERAGE" % read_dir,
        ]

    _val = [
        "GPRINT:system:MIN:%8.2lf",
        "GPRINT:system:MAX:%8.2lf",
        "GPRINT:system:AVERAGE:%8.2lf",
        "GPRINT:system:LAST:%8.2lf\\n",
        ]

    _area = []
    if last is True:
        _area = [
            "AREA:system#8FC31F:System   ",
            ]
    if last is False:
        _val = ["STACK:system#8FC31F:System   "] + _val

    return (_def, _val, _area)

def make_softirq(read_dir, last=False):

    _def = [
            "DEF:softirq=%s/cpu-softirq.rrd:value:AVERAGE" % read_dir,
        ]

    _val = [
            "GPRINT:softirq:MIN:%8.2lf",
            "GPRINT:softirq:MAX:%8.2lf",
            "GPRINT:softirq:AVERAGE:%8.2lf",
            "GPRINT:softirq:LAST:%8.2lf\\n",
        ]

    _area = []
    if last is True:
        _area = [
            "AREA:softirq#1D2088:SoftIRQ  ",
            ]
    if last is False:
        _val = ["STACK:softirq#1D2088:SoftIRQ  "] + _val

    return (_def, _val, _area)

def make_steal(read_dir, last=False):
    _def = [
        "DEF:steal=%s/cpu-steal.rrd:value:AVERAGE" % read_dir,
        ]

    _val = [
        "GPRINT:steal:MIN:%8.2lf",
        "GPRINT:steal:MAX:%8.2lf",
        "GPRINT:steal:AVERAGE:%8.2lf",
        "GPRINT:steal:LAST:%8.2lf\\n",
        ]

    _area = []
    if last is True:
        _area = [
            "AREA:steal#E5006A:Steal    ",
            ]

    if last is False:
        _val = ["STACK:steal#E5006A:Steal    "] + _val


    return (_def, _val, _area)


def graph(read_dir, write_dir, category, start, end, types=None, size="small"):
    print types
    read_dir = str(read_dir)

    options = RRD[size]

    if os.path.isdir(read_dir) is False:
        print "read_dir error"


    write_file_path = "%s/%s.png" % (write_dir, generate_phrase(12))

    # generate rrd graph params
    if types is None:
        types = DEFAULT_TYPES


    _setting = [
        "--font", options["font"],
        "--title", str(category),
        "--vertical-label", "jiffies",
        "--upper-limit", "100",
        "--rigid",
        "--width", options["width"],
        "--height", options["height"],
        "--color", "BACK#DCDDDD",
        "--color", "CANVAS#FFFFFF",
        "--color", "GRID#BDC3C4",
        "--color", "MGRID#CCCCCC",
        "--color", "FONT#006083",
        "--color", "ARROW#006083",
        "--color", "FRAME#FFFFFF",
        "--color", "SHADEA#FFFFFF",
        "--color", "SHADEB#FFFFFF",
        "--start", start,
        "--end",   end,
        "--legend-direction", "bottomup",
        ]
    _area = [
        ]
    _comment = [
        "COMMENT:%s" % options["comment"],
        "COMMENT: \\n"
        ]


    _def = []
    _val = []
    for i in xrange(len(types)):
        fn = getattr(akiyoshi.plugins["rrd"][TYPE], "make_"+types[i])
        if i == len(types)-1:
            (__def, __val, __area) = fn(read_dir, True)
        else:
            (__def, __val, __area) = fn(read_dir)

        _def = _def + __def
        _val = __val + _val
        if __area and 0 < len(__area):
            _area = __area


    param = [write_file_path] + _setting + _def + _area + _val + _comment
    for x in param: print x
    
    rrdtool.graph(param)
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
