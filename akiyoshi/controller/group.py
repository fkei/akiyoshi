import web
from lib.rest import Rest, auth
from service.group import groupService

class GroupController(Rest):

    @auth
    def _GET(self, *param, **params):
        self.__template__.media = "json"
        category = None
        if param[0]:
            category = param[0]

        categorys = groupService.find(web.ctx.orm, category)
        self.view = []
        for category in categorys:
            self.view.append(category.json())

        return True

urls = ('/group/([a-zA-Z0-9-_. ]+)/?', GroupController)
