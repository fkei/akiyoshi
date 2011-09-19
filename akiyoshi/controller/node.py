# 3rd party
import web

from lib.rest import Rest, auth
import akiyoshi
from service.node import nodeService

class NodeController(Rest):

    @auth
    def _GET(self, *param, **params):
        basedir = akiyoshi.config.collectd["basedir"]
        self.__template__.media = "json"

        if len(param) == 1:
            (ctlnodes, fsnodes) = nodeService.nodeGroup(web.ctx.orm, basedir, param[0])
        else:
            (ctlnodes, fsnodes) = nodeService.nodes(web.ctx.orm, basedir)

        self.view = []

        if fsnodes is None:
            return True

        for fsnode in fsnodes:
            ret = None
            for ctlnode in ctlnodes:
                if fsnode == ctlnode.host:
                    tags = []
                    for tag in ctlnode.tags:
                        tags.append(tag.name)

                    ret = ({
                        "name": fsnode,
                        "control": True,
                        "notebook": ctlnode.notebook.value,
                        "tags": tags
                        })
            if ret is None:
                self.view.append({
                    "name": fsnode,
                    "control": False,
                    "notebook": "",
                    "tags": []
                    })
            else:
                self.view.append(ret)

        return True

    @auth
    def _POST(self, *param, **params):
        host = self.input.host
        notebook = self.input.notebook
        category = self.input.category
        tags = self.input.tags

        node = nodeService.save(web.ctx.orm, self.me, host, notebook, category, tags)

        return True

urls = ('/node/?', NodeController,
        r"/node/([a-zA-Z0-9-_. ]+)/?", NodeController)
