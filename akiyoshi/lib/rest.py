#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import traceback

# 3rd party
import web
from web.contrib.template import render_mako

from mako.template import Template
from mako.lookup import TemplateLookup
from mako import exceptions

import akiyoshi

class Rest:
    def __init__(self):
        self.log = akiyoshi.log
        self.__template__ = web.Storage()
        self.__template__.dir = self.__class__.__name__.lower()
        self.__template__.file = self.__class__.__name__.lower()
        self.__template__.media = 'html'

        self.view = web.Storage()

    def _pre(self, *param, **params):
        pass

    def _post(self, f):
        now = datetime.now()
        web.lastmodified(now)
        web.httpdate(now)

        web.header('Cache-Control', 'no-cache,private')
        web.header('Pragma', 'no-cache')

        if isinstance(f, web.HTTPError) is True:
            raise f

        if f is True:
            path = '%s/%s.%s' % (
                self.__template__.dir,
                self.__template__.file,
                self.__template__.media)

        try:
            _r = self.__mako_render(path,
                             title='akiyoshi', view=self.view)
            return _r
        except:
            return exceptions.html_error_template().render(full=True)

    def GET(self, *param, **params):
        try:
            self._pre(*param, **params)
            self.__method__ = 'GET'
            _r = self.__method_call(prefix='_', *param, **params)
            return self._post(_r)
        except web.HTTPError, e:
            raise
        except:
            self.log.error(traceback.format_exc())
            #return web.internalerror()
            raise

    def PUT(self, *param, **params):
        try:
            self.__method__ = 'PUT'
            self._pre(*param, **params)
            _r = self.__method_call(prefix='_', *param, **params)
            return self._post(_r)
        except web.HTTPError, e:
            raise
        except:
            self.log_trace.error(traceback.format_exc())
            #return web.internalerror()
            raise

    def DELETE(self, *param, **params):
        try:
            self.__method__ = 'DELETE'
            self._pre(*param, **params)
            _r = self.__method_call(prefix='_', *param, **params)
            return self._post(_r)
        except web.HTTPError, e:
            raise
        except:
            self.log.error(traceback.format_exc())
            #return web.internalerror()
            raise

    def POST(self, *param, **params):
        try:
            if web.input(_unicode=False).has_key('_method'):
                self.__method__ = web.input(_unicode=False)['_method'].upper()
                if self.__method__ == 'PUT':
                    self.__method__ = 'PUT'
                    self.log.debug("OVERLOAD - POST -> PUT")
                    return self.__method_call(*param, **params)
                elif self.__method__ == 'DELETE':
                    self.__method__ = 'DELETE'
                    self.log.debug("OVERLOAD - POST -> DELETE")
                    return self.__method_call(*param, **params)
                elif self.__method__ == 'GET':
                    self.__method__ = 'GET'
                    self.log.debug("OVERLOAD - POST -> GET")
                    return self.__method_call(*param, **params)

            # POST Method
            self.__method__ = 'POST'
            self._pre(*param, **params)
            _r = self.__method_call(prefix='_', *param, **params)
            return self._post(_r)
        except web.HTTPError, e:
            raise
        except:
            self.log.error(traceback.format_exc())
            #return web.internalerror()
            raise

    def __method_call(self, *param, **params):
        if params.has_key('prefix'):
            prefix = params.pop('prefix')
        else:
            prefix = ''

        try:
            if hasattr(self, prefix + self.__method__) is True:
                method = getattr(self, prefix + self.__method__)
                return method(*param, **params)
            else:
                self.log.debug('%s : Method=%s - Not Method' %
                                  (str(self), self.__method__))
                return web.nomethod()
        except:
            self.log.error("__method_call() error - prefix=%s" \
                              % (str(prefix)))
            raise

    def __mako_render(rest, templatename, **kwargs):
        """Template Engine
        """
        if templatename.startswith('static/') is True:
            directories = [akiyoshi.dirname, 'static', templatename[7:]]
            filepath = '/'.join(directories)
            rest.log.debug(filepath)

            fp = open(filepath, "r")
            try:
                return fp.read()
            finally:
                fp.close()

        else:
            directories = [akiyoshi.dirname, 'templates']
            if akiyoshi.config.has_key('theme'):
                directories.append(akiyoshi.config['theme'])
            else:
                directories.append('default')

        tl = TemplateLookup(directories='/'.join(directories),
                            input_encoding='utf-8',
                            output_encoding='utf-8',
                            default_filters=['decode.utf8'],
                            encoding_errors='replace')

        try:
            t = tl.get_template(templatename)
        except exceptions.TopLevelLookupException, tlle:
            rest.log.error('We could not find the template directory. - %s/%s'
                         % ('/'.join(directories), templatename))
            return web.notfound()

        rest.log.info('Template file path=%s' % t.filename)

        view = {}
        if kwargs.has_key('view'):
            for x in kwargs['view'].keys():
                view[x] = kwargs['view'][x]
            kwargs.pop('view')

        kwargs.update(view)
        return t.render(**kwargs)


# -- HTTP Status Code
class Unauthorized(web.HTTPError):
    def __init__(self, data='unauthorized'):
        if isinstance(data, list):
            data = "\n".join(data)

        global BASIC_REALM
        status = "401 Unauthorized"
        headers = {
            'Content-Type': 'text/html; charset=utf-8',
            'WWW-Authenticate': 'Basic realm="%s"' % BASIC_REALM
        }
        web.HTTPError.__init__(self, status, headers, data)

web.unauthorized = Unauthorized

class Conflict(web.HTTPError):
    def __init__(self, url, data='conflict'):
        if isinstance(data, list):
            data = "\n".join(data)

        status = "409 Conflict"
        headers = { 
            'Content-Type': 'text/html; charset=utf-8',
        }
        headers['Location'] = url
        web.HTTPError.__init__(self, status, headers, data)

web.conflict = Conflict

class Created(web.HTTPError):
    def __init__(self, url, data='created'):
        if isinstance(data, list):
            data = "\n".join(data)

        status = "201 Created"
        headers = {
            'Content-Type': 'text/html; charset=utf-8',
            'Location': url
        }
        web.HTTPError.__init__(self, status, headers, data)

web.created = Created

class Accepted(web.HTTPError):
    def __init__(self, data='accepted', url=None):
        if isinstance(data, list):
            data = "\n".join(data)

        status = "202 Accepted"
        headers = {
                'Content-Type': 'text/html; charset=utf-8',
        }
        if url:
            headers['Location'] = url
        web.HTTPError.__init__(self, status, headers, data)

web.accepted = Accepted

class NoContent(web.HTTPError):
    def __init__(self):
        status = "204 No Content"
        headers = {
            'Content-Type': 'text/html; charset=utf-8',
        }
        web.HTTPError.__init__(self, status, headers)

web.nocontent = NoContent

#class RequestTimeout(web.HTTPError):
#    def __init__(self):
#        status = "408 Request Timeout"
#        web.HTTPError.__init__(self, status)
#
#web.requesttimeout = RequestTimeout

def NotFound(data = None):
    if isinstance(data, list):
        data = "\n".join(data)

    return web.NotFound(data)

web.notfound = NotFound

def InternalError(data = None):
    if isinstance(data, list):
        data = "\n".join(data)

    return web.InternalError(data)

web.internalerror = InternalError

class BadRequest(web.HTTPError):
    def __init__(self, data="bad request"):
        if isinstance(data, list):
            data = "\n".join(data)

        status = "400 Bad Request"
        headers = {'Content-Type': 'text/html'}
        web.HTTPError.__init__(self, status, headers, data)

web.badrequest = BadRequest



if __name__ == "__main__":
    pass

