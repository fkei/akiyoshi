import web
from lib.rest import Rest

class Home(Rest):

    def _GET(self, *param, **params):
        return True

urls = ('/', Home)
