import web
from lib.rest import Rest

class HomeController(Rest):

    def _GET(self, *param, **params):
        return True

urls = ('/', HomeController)
