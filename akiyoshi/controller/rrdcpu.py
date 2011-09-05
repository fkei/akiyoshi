import web
from lib.rest import Rest

class RrdCpu(Rest):

    def _GET(self, *param, **params):
        self.download.type = self.DOWNLOAD_TYPE_FILE
        self.download.file = "/var/collectd/xxx/cpu-%s/cpu-%s.rrd" % (param[0], param[1])
        self.log.debug("Download rrd file. %s" % self.download.file)
        return True

#/rrd/cpu/0/idle
urls = ("/rrd/cpu/(\d+)/([_a-zA-Z0-9-_]+)", RrdCpu)
