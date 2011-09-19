class Model(object):
    def utf8(self, column):
        if hasattr(self, column):
            ret = getattr(self, column)
            if isinstance(ret, unicode):
                return ret.encode('utf-8')
            elif isinstance(ret, str):
                return ret
            else:
                return str(ret)
        else:
            raise 'column not found.'


