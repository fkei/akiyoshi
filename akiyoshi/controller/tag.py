# 3rd party
import web

from lib.rest import Rest, auth
import akiyoshi
from service.tag import tagService

class TagController(Rest):

    @auth
    def _GET(self, *param, **params):
        pass

urls = ('/tag/?', TagController)
        #'/tag/([_a-zA-Z0-9-_.]+)/?', TagController)
