# 3rd party
import web

from lib.rest import Rest
import akiyoshi
from service.node import nodeService

class NodeController(Rest):

    def _GET(self, *param, **params):
        basedir = akiyoshi.config.collectd["basedir"]
        self.__template__.media = "json"

        if 0 < len(param):
            # Specify host
            self.view = nodeService.list("%s/%s" % (basedir, param[0]))
            return True
        else:
            # all
            self.view = nodeService.list(basedir)
            return True

urls = ('/node/?', NodeController,
        '/node/([_a-zA-Z0-9-_.]+)/?', NodeController)
