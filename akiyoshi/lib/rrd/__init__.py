#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import rrdtool

from lib.const import rrd
from lib.common import generate_phrase

def fetch(rrdfiles, type, resolution, start, end):
    # rrdtool fetch cpu-idle.rrd AVERAGE --resolution=300 --start=1316691346 --end=1316777746
    print "%s %s --resolution %s --start %s --end %s" % (str(rrdfiles[0]), type, resolution, start, end)
    data = rrdtool.fetch(str(rrdfiles[0]),
                         type,
                         "--resolution", str(resolution),
                         "--start", start,
                         "--end", end
                         )
    return data

