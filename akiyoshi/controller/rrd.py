import web
from lib.rest import Rest

class Rrd(Rest):

    def _GET(self, *param, **params):
        self.download.type = self.DOWNLOAD_TYPE_FILE
        self.download.file = "/var/collectd/xxx/cpu-0/cpu-idle.rrd"
        
        return True

urls = ("/rrd/[_a-zA-Z0-9-_]+/", Rrd)
