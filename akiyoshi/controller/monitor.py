import web
from lib.rest import Rest, auth

import akiyoshi
from service.monitor import monitorService

class Monitor(Rest):

    @auth
    def _GET(self, *param, **params):
        self.__template__.media = "json"
        basedir = akiyoshi.config.collectd["basedir"]
        category = None
        if 1 == len(param):
            # /(host|category)/*
            category = param[0]
        else:
            return web.notfound() # TODO

        # tag(category)
        monitors = monitorService.controlList(web.ctx.orm, basedir, category, True)
        if monitors["node"]:
            self.view = monitors
            self.view["type"] = "tag"
            return True

        # host
        directory = "%s/%s" % (basedir, category)
        monitors = monitorService.list(web.ctx.orm, basedir, category, True)
        self.view["type"] = "host"
        self.view = monitors

        return True



        """
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
        """

urls = (r"/monitor/([a-zA-Z0-9-_. ]+)/?", Monitor)
