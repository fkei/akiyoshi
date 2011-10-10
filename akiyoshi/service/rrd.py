import os
import os.path
import re

from lib.common import pastany_epochsec, \
     past1_epochsec, \
     past7_epochsec, \
     past30_epochsec, \
     past365_epochsec, \
     past1hour_epochsec, \
     past12hour_epochsec, \
     epochsec2strftime
from lib.const import format
import akiyoshi

from service.plugin import pluginService

class RrdService:

    def graph(self, write_dir, basedir, host, category, start, end, size="small"):

        plugin = pluginService.getRrdType(category)

        read_dir = "%s/%s/%s" % (basedir, host, category)

        path = plugin.graph(read_dir, write_dir, category, start, end, size)

        return path

    def _analysisInterval(self, interval):
        _interval = "1day" # default

        if interval == "1hour":
            (start, end) = past1hour_epochsec()
            _interval = "1hour"

        elif interval == "12hour":
            (start, end) = past12hour_epochsec()
            _interval = "12hour"

        elif interval == "1day":
            (start, end) = past1_epochsec()
            _interval = "1day"

        elif interval == "7day":
            (start, end) = past7_epochsec()
            _interval = "7day"

        elif interval == "30day":
            (start, end) = past30_epochsec()
            _interval = "30day"

        elif interval == "365day":
            (start, end) = past365_epochsec()
            _interval = "365day"

        else:
            try:
                day = int(interval.replace("day", ""))
                _interval = "1day"
                (start, end) = pastany_epochsec(day)
            except:
                day = 1
                _interval = "1day"
                (start, end) = pastany_epochsec(day)

        return (_interval, start, end)

    def fetch(self, rrdfiles, type, resolution, interval):
        (interval, start, end) = self._analysisInterval(interval)

        plugin = pluginService.getRrd()
        datas = plugin.fetch(rrdfiles, type, resolution, start, end)

        ret = self._formatting(rrdfiles, datas, interval)
        return ret


    def _formatting(self, rrdfiles, datas, str_interval):
        """rrd dump formatting
        """
        ret = {}
        ret["interval"] = str_interval
        ret["format"] = format["rrd"][str_interval]
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

                #epochsec = start+(interval*i)
                #strnow = epochsec2strftime(epochsec, ret["format"])
                epoch = long(start+interval*i) * 1000L

                if data[2][i][0] is None:
                    _d.append([epoch, 0])
                else:
                    #_d.append(float("%.2f" % data[2][i][0]))
                    _d.append([epoch, data[2][i][0]])
                    #_d.append([strnow, data[2][i][0]])

            ret["datasets"][name]["data"] = _d

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

