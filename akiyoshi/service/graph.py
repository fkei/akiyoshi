import os
import os.path

from lib.rrd import cpu

class GraphService:

    def make(self, write_dir, basedir, host, category, start, end, size="small"):
        read_dir = "%s/%s/%s" % (basedir, host, category)
        path = cpu.make(read_dir, write_dir, category, start, end, size)
        print path
        return path

graphService = GraphService()
