import web
from lib.rest import Rest, auth

class HomeController(Rest):

    @auth
    def _GET(self, *param, **params):
        return True

urls = ('/', HomeController)
