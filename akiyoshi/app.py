#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import traceback

# 3rd party
try:
    import web
    import mako
    import sqlalchemy
    import simplejson
except ImportError, e:
    print >>sys.stderr, '[ERROR] Libraries are missing. - %s' % ''.join(e.args)
    sys.exit(1)

import akiyoshi
import processor
import bootstrap
import urls
import plugin

def main():
    if bootstrap.start() is False:
        sys.exit(1)

    # web
    app = web.application(urls.load(), globals(), autoreload=True)
    app.internalerror = web.debugerror
    sys.argv = [] # web.py argv clean.

    # load processor!!
    app.add_processor(processor.load_database)

    # load plugin
    plugin.load()
    
    # start
    try:
        akiyoshi.log.info("akiyoshi web server start.")
        app.run()
    except Exception, e:
        akiyoshi.log.critical(traceback.format_exc())
        print >>sys.stderr, "[ERROR] %s" % str(e.args)
        print >>sys.stderr, traceback.format_exc()
        return 1

if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception, e:
        print sys.stderr, traceback.format_exc()
        sys.exit(1)
