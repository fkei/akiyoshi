import web
from lib.rest import Rest, auth

import akiyoshi
from service.graph import graphService
from service.rrd import rrdService
from service.node import nodeService

from lib.common import now_epochsec, past1_epochsec

class Graph(Rest):

    @auth
    def _GET(self, *param, **params):
        basedir = akiyoshi.config.collectd["basedir"]

        if 3 == len(param):
            if param[2] == "png":
                # rrd graph
                if self.input.has_key("interval"):
                    interval = self.input.interval
                else:
                    interval = "1day"

                if self.input.has_key("types") and 0 < len(self.input.types):
                    types = self.input.types.split(",")
                else:
                    types = None

                # image
                (start, end) = past1_epochsec()
                size = "normal-wide"

                output = rrdService.graph(akiyoshi.config.tmp,
                                          basedir,
                                          param[0],
                                          param[1],
                                          interval,
                                          types,
                                          size)

                self.download.file = output
                self.download.type = self.DOWNLOAD_TYPE_FILE
                self.download.once = True
            elif param[2] == "dat":
                # rrd fetch
                targetdir = "%s/%s/%s" % (basedir, param[0], param[1])
                rrdfiles = nodeService.fsnodes(targetdir)
                fullRrdFiles = []
                for rrdfile in rrdfiles:
                    fullRrdFiles.append(str("%s/%s/%s/%s" % (basedir, param[0], param[1], rrdfile)))

                if self.input.has_key("type"):
                    type = self.input.type
                else:
                    type = "AVERAGE"


                if self.input.has_key("resolution"):
                    resolution = self.input.resolution
                else:
                    resolution = "300"

                if self.input.has_key("interval"):
                    interval = self.input.interval
                else:
                    interval = "1day"

                data = rrdService.fetch(fullRrdFiles, type, resolution, interval)

                self.__template__.media = "json"
                self.view = data

                return True

            else:
                return web.notfound() # TODO
        else:
            # Unsure
            return web.notfound() # TODO

class GraphGroup(Rest):

    @auth
    def _GET(self, *param, **params):
        basedir = akiyoshi.config.collectd["basedir"]

        data = graphService.getGraphLinks(web.ctx.orm, basedir,param[0], param[1])
        self.__template__.media = "json"
        self.view = data
        return True

urls = (r"/graph/([a-zA-Z0-9-_.]+)/([a-zA-Z0-9-_.]+)\.(dat|png)$", Graph,
        r"/graph/([a-zA-Z0-9-_.]+)/([a-zA-Z0-9-_.]+)/?", GraphGroup)
