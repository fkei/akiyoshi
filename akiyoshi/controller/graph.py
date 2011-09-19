import web
from lib.rest import Rest, auth

import akiyoshi
from service.graph import graphService
from lib.common import now_epochsec, pastday_epochsec

class Graph(Rest):

    @auth
    def _GET(self, *param, **params):
        basedir = akiyoshi.config.collectd["basedir"]

        if 3 == len(param):
            # rrd graph
            (end, start) = pastday_epochsec()
            size = "normal"
            output = graphService.make(akiyoshi.config.tmp,
                                       basedir,
                                       param[0],
                                       param[1],
                                       start,
                                       end,
                                       size)
            self.download.file = output
            self.download.type = self.DOWNLOAD_TYPE_FILE
            self.download.once = True
        else:
            # Unsure
            return web.notfound() # TODO

urls = (r"/graph/([a-zA-Z0-9-_.]+)/([a-zA-Z0-9-_.]+)(\.png)$", Graph)
