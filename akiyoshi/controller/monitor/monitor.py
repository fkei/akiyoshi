import web
from lib.rest import Rest, auth

import akiyoshi
from service.monitor import monitorService

class MonitorController(Rest):

    @auth
    def _GET(self, *param, **params):
        return True

class MonitorBy1Controller(Rest):

    @auth
    def _GET(self, *param, **params):
        self.__template__.media = "json"
        basedir = akiyoshi.config.collectd["basedir"]
        category = None
        if 1 == len(param):
            # /(host|category|hosts)/*
            category = param[0]
        else:
            return web.notfound() # TODO

        # group|compare
        if self.input.has_key("type") is False:
            # TODO error
            return False
        
        type = self.input.type

        if type == "group":
            # group
            hosts = category.split(",")
            if 1 < len(hosts):
                monitors = monitorService.groupList(basedir, hosts, True)
                if monitors["node"]:
                    self.view = monitors
                    self.view["type"] = "compare"
                    return True

            # TODO error
            return False
        elif type == "compare":
            # compare
            hosts = category.split(",")
            if 1 < len(hosts):
                monitors = monitorService.compareList(basedir, hosts, True)
                if monitors["node"]:
                    self.view = monitors
                    self.view["type"] = "compare"
                    return True

            # TODO error
            return False
            
        elif type == "tag":
            # tag(category)
            monitors = monitorService.tagList(web.ctx.orm, basedir, category, True)
            if monitors["node"]:
                self.view = monitors
                self.view["type"] = "tag"
                return True

            # TODO error
            return False

        # host (default)
        directory = "%s/%s" % (basedir, category)
        monitors = monitorService.list(web.ctx.orm, basedir, category, True)
        self.view["type"] = "host"
        self.view = monitors

        return True

urls = (r"/monitor/?", MonitorController,
        r"/monitor/([a-zA-Z0-9-_. ,]+)/?", MonitorBy1Controller)
