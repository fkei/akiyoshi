import web

from lib.rest import Rest
import akiyoshi
from service.manager import managerService

class ManagerController(Rest):

    def _GET(self, *param, **params):
        basedir = akiyoshi.config.collectd["basedir"]
        self.__template__.media = "json"

        (control, fs) = managerService.nodes(web.ctx.orm, basedir)
        self.view = []
        for node in fs:
            if node in control:
                self.view.append({
                    "name": node,
                    "control": True
                    })
            else:
                self.view.append({
                    "name": node,
                    "control": False
                    })
        
        return True

urls = ('/manager/?', ManagerController,
        '/manager/node/?', ManagerController)
