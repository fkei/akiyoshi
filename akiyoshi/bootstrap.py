import sys
import os.path
from os import environ as env
import traceback
from optparse import OptionParser, OptionValueError
import logging
import logging.config

# 3rd party
import simplejson

import akiyoshi

__usage__="akiyoshi"

def getopts():
    """parse command options.
    """
    optp = OptionParser(usage=__usage__, version=akiyoshi.__version__)
    optp.add_option('-c', '--config', dest='config', help='Configuration file path.')
    return optp.parse_args()

def checkopts(opts):
    """option check.
    """
    pass

def load(file):
    """Reading the configuration file
    """
    absfile = os.path.abspath(file)
    fp = open(absfile)
    return simplejson.load(fp)

def start():
    """startup
    """
    # init
    import web
    akiyoshi.Storage = web.Storage

    # options
    (opts, args) = getopts()
    if opts.config:
        if checkopts(opts.config): return False
        akiyoshi.options = opts
        # config
        akiyoshi.config = akiyoshi.Storage(load(akiyoshi.options.config))

        # logging
        if os.path.isfile(akiyoshi.config["log"]["file"]) is False:
            print >>sys.stderr, 'logging file not found. %s' % akiyoshi.config["log"]["file"]

        logging.config.fileConfig(akiyoshi.config["log"]["file"])
        print >>sys.stdout, 'logging file loading. %s' % akiyoshi.config["log"]["file"]
        akiyoshi.log = logging.getLogger('akiyoshi.default')

        # external search path
        for y in [x.strip() for x in akiyoshi.config["external"]["searchpath"].split(',') if x]:
            if (y in sys.path) is False: sys.path.insert(0, y)

        # python search path
        sys.path.insert(0, akiyoshi.dirname)

    else:
        print >>sys.stderr, '[ERROR] Please specify the configuration file path. -c or --config'
        return False

