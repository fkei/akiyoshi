import os
import re
import sys

import akiyoshi

def load():
        # load plugin
        for x in akiyoshi.config.plugin:
            akiyoshi.plugins[x] = {}
            akiyoshi.plugins[x]["self"] = __import__("plugin/%s" % (x))

            for y in akiyoshi.config.plugin[x]:
                try:
                    akiyoshi.plugins[x][y] = __import__("plugin/%s/%s" % (x, y))
                    print >>sys.stdout, "[INFO] load plugin.  %s:%s" % (x, y)
                except ImportError, ie:
                    print >>sys.stdout, "[WARN] not load plugin.  %s:%s" % (x, y)

if __name__ == "__main__":
    pass
