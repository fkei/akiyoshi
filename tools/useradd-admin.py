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


# Relative path
sys.path.insert(0, "../akiyoshi")

import akiyoshi
import bootstrap
import db
from service.user import userService

def main():
    if bootstrap.start() is False:
        sys.exit(1)

    # start
    try:
        session = db.get_session()
        user = userService.merge(session,
                                 akiyoshi.config["admin"]["user"],
                                 akiyoshi.config["admin"]["password"],
                                 "Administrator")

        try:
            session.commit()
            return 0
        except sqlalchemy.exceptions.IntegrityError, e:
            print >>sys.stderr, "[ERROR] %s" % str(e)
            return 1

    except Exception, e:
        akiyoshi.log.critical(traceback.format_exc())
        print >>sys.stderr, "[ERROR] %s" % str(e.args)
        print >>sys.stderr, traceback.format_exc()
        return 1

if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception, e:
        print >>sys.stderr, traceback.format_exc()
        sys.exit(1)
