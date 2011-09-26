import os
import os.path
import re

from lib.common import pastany_epochsec, past1_epochsec, past7_epochsec, past30_epochsec, past365_epochsec
import lib.rrd
from lib.rrd import cpu

class RrdService:

    def make(self, write_dir, basedir, host, category, start, end, size="small"):
        read_dir = "%s/%s/%s" % (basedir, host, category)
        path = cpu.make(read_dir, write_dir, category, start, end, size)
        print path
        return path

    def fetchTime(self, rrdfiles, type, resolution, start, end):
        pass

    def fetch(self, rrdfiles, type, resolution, interval):
        if interval == "1day":
            (start, end) = past1_epochsec()
        elif interval == "7day":
            (start, end) = past7_epochsec()
        elif interval == "30day":
            (start, end) = past30_epochsec()
        elif interval == "365day":
            (start, end) = past365_epochsec()
        else:
            try:
                day = int(interval.replace("day", ""))
            except:
                day = 1
            (start, end) = pastany_epochsec(day)

        datas = lib.rrd.fetch(rrdfiles, type, resolution, start, end)
        return self._formatting(rrdfiles, datas)


    def _formatting(self, rrdfiles, datas):
        """rrd dump formatting
        """
        ret = {}
        ret["rrd"] = {}
        ret["datasets"] = {}
        #ret["type"] = type

        for rrdfile in rrdfiles:
            # ((1316691840, 1316778720, 480), ('value',), [(99.457395833333337,), ...
            data = datas[rrdfile]
            (type, name) = self._getSelection(rrdfile)

            # rrd
            ret["rrd"][name] = {}
            ret["rrd"][name]["setting"] = data[0]
            ret["rrd"][name]["column"] = data[1]

            # datasets
            ret["datasets"][name] = {}
            ret["datasets"][name]["label"] = name + " = 0"

            start = data[0][0]
            end = data[0][1]
            interval = data[0][2]
            _d = []
            for i in xrange(0, len(data[2])):
                if data[2][i][0] is None:
                    _d.append([start+(interval*i), 0])
                else:
                    #_d.append(float("%.2f" % data[2][i][0]))
                    _d.append([start+(interval*i), data[2][i][0]])

            ret["datasets"][name]["data"] = _d
            #print len(ret["datasets"][name]["data"])

        return ret

    def _getSelection(self, rrdfile):
        """ example) type=cpu, name=idle
        """
        name = os.path.splitext(os.path.basename(rrdfile))[0]
        idx = name.find("-")
        type = name[:idx]
        name = name[idx+1:]
        return type, name

rrdService = RrdService()

