import web
from lib.rest import Rest, auth

import akiyoshi
from service.node import nodeService
from service.monitor.graph import graphService
from service.monitor.rrd import rrdService

from lib.common import now_epochsec, past1_epochsec

class GraphController(Rest):

    @auth
    def _GET(self, *param, **params):
        basedir = akiyoshi.config.collectd["basedir"]
        
        if 3 != len(param):
            # Unsure
            return web.notfound() # TODO

        if self.input.has_key("type") is False:
            # TODO
            return False

        type = self.input.type
        host = param[0]
        category = param[1]
        media = param[2]

        if media == "png":
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
                                      host,
                                      category,
                                      interval,
                                      type,
                                      types,
                                      size)

            self.download.file = output
            self.download.type = self.DOWNLOAD_TYPE_FILE
            self.download.once = True

        elif media == "dat":
            # rrd fetch
            targetdir = "%s/%s/%s" % (basedir, host, category)
            rrdfiles = nodeService.fsnodes(targetdir)
            fullRrdFiles = []

            for rrdfile in rrdfiles:
                fullRrdFiles.append(str("%s/%s/%s/%s" \
                                        % (basedir, host, category, rrdfile)))

            if self.input.has_key("fn"):
                fn = self.input.fn
            else:
                fn = "AVERAGE"

            if self.input.has_key("resolution"):
                resolution = self.input.resolution
            else:
                resolution = "300"

            if self.input.has_key("interval"):
                interval = self.input.interval
            else:
                interval = "1day"

            data = rrdService.fetch(fullRrdFiles, fn, resolution, interval, type)

            self.__template__.media = "json"
            self.view = data

            return True

        else:
            return web.notfound() # TODO

class GraphGroupController(Rest):

    @auth
    def _GET(self, *param, **params):

        basedir = akiyoshi.config.collectd["basedir"]
        if self.input.has_key("type") is True:
            type = self.input.type
        else:
            type = None

        host = param[0]
        category = param[1]
        data = graphService.getGraphLinks(web.ctx.orm, basedir, host, category, type)
        self.__template__.media = "json"
        self.view = data
        return True

urls = (r"/graph/([a-zA-Z0-9-_. ,]+)/([a-zA-Z0-9-_.]+)\.(dat|png)$", GraphController,
        r"/graph/([a-zA-Z0-9-_. ,]+)/([a-zA-Z0-9-_.]+)/?", GraphGroupController)
