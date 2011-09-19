#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from base64 import b64decode

import web

import akiyoshi
from service.user import userService
from lib.const import system
from lib.common import mktmp

def auth(func):

    def wrapper(self, *args, **kwargs):
        # -- Basic Auth
        def __login():
            _http_auth = web.ctx.env['HTTP_AUTHORIZATION'].strip()
            if _http_auth[:5] == 'Basic':
                email, password = b64decode(_http_auth[6:].strip()).split(':')
                session = web.ctx.orm
                user = userService.login(session, unicode(email), unicode(password))
                return (user, email)

        if web.ctx.env.has_key('HTTP_AUTHORIZATION'):
            (user, email) = __login()

            if user:
                self.me = user

                # Logout
                fname = '%s%s' % (mktmp(), self.me.email,)
                if os.access(fname, os.F_OK):
                    os.unlink(fname)
                    return web.unauthorized()

                # Login: Success
                akiyoshi.log.info('user_id=%s, method=%s - Basic Authentication=Success' %
                                  (self.me.id, self.__method__))

                # __init__#self._ update!!
                return func(self, *args, **kwargs)
            else:
                 # Login: Failure
                akiyoshi.log.info('user=%s, method=%s - Basic Authentication=Failure' %
                                  (email, self.__method__))
                return web.unauthorized()
        else:
            # Login: Anonymous
            akiyoshi.log.info('user=anonymous, method=%s - Basic Authentication=Anonymous' %
                              (self.__method__))
            return web.unauthorized()

    wrapper.__name__ = func.__name__
    wrapper.__dict__ = func.__dict__
    wrapper.__doc__ = func.__doc__
    return wrapper

