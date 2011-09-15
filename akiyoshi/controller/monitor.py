import web
from lib.rest import Rest

import akiyoshi
from service.monitor import monitorService

class Monitor(Rest):

    def _GET(self, *param, **params):

        basedir = akiyoshi.config.collectd["basedir"]
        host = None
        category = None
        name = None

        if 1 == len(param):
            # /host/*
            host = param[0]
        else:
            return web.notfound() # TODO

        directory = "%s/%s" % (basedir, host)
        monitors = monitorService.list(directory, False)
        self.view = {}

        self.__template__.media = "json"
        for monitor in monitors:
            self.view[monitor] = {}
            if 1 == len(param):
                # redirect
                self.view[monitor]["url"] = "%s/graph/%s/%s.png" % (web.ctx.homedomain, host, monitor)
                self.view[monitor]["type"] = "monitor"
            elif 0 == len(param):
                # redirect
                self.view[monitor]["url"] = "%s/monitor/%s" % (web.ctx.homedomain, monitor)
                self.view[monitor]["type"] = "monitor"
            else:
                web.notfound() # TODO


        return True

urls = (r"/monitor/([a-zA-Z0-9-_.]+)/?", Monitor)
