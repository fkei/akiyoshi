import web
from lib.rest import Rest

import akiyoshi
from service.node import nodeService

class Rrd(Rest):

    def _GET(self, *param, **params):
        basedir = akiyoshi.config.collectd["basedir"]
        host = None
        category = None
        name = None

        if 1 == len(param):
            # /host/*
            host = param[0]
        elif 2 == len(param):
            # /host/category/*
            category = param[1]
        else:
            return web.notfound() # TODO

        rrds = nodeService.list(basedir, host, category)
        self.view = {}
 
        self.__template__.media = "json"
        for rrd in rrds:
            self.view[rrd] = {}
            if 1 == len(param):
                # redirect
                self.view[rrd]["url"] = "%s/graph/%s/%s" % (web.ctx.homedomain, host, rrd)
                self.view[rrd]["type"] = "rrd"
            elif 0 == len(param):
                # redirect
                self.view[rrd]["url"] = "%s/rrd/%s" % (web.ctx.homedomain, rrd)
                self.view[rrd]["type"] = "rrd"
            else:
                web.notfound() # TODO


        return True

urls = ("/rrd/?", Rrd,
        r"/rrd/([a-zA-Z0-9-_.]+)/?", Rrd)
