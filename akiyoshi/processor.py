
# 3rd party
import web

import akiyoshi
import db

def load_database(handler):
    """ HTTP Request -Thread-local
    """
    web.ctx.orm = db.get_session()

    akiyoshi.log.debug('Database session scope [start] - %s' % web.ctx.orm)
    try:
        ret = handler()
        web.ctx.orm.commit()
        akiyoshi.log.debug('Database session scope [commit] - %s' % web.ctx.orm)

        return ret
    except web.HTTPError:
        if web.ctx.status[:1] in ['2', '3']:
            web.ctx.orm.commit()
            akiyoshi.log.debug('Database session scope [commit] : HTTP Status=%s - %s'
                               % (web.ctx.status, web.ctx.orm))
            raise
        else:
            web.ctx.orm.rollback()
            akiyoshi.log.debug(
                'Database session scope [rollback] : HTTP Status=%s - %s'
                % (web.ctx.orm, web.ctx.status))
            raise
    except:
        web.ctx.orm.rollback()
        akiyoshi.log.debug('Database session scope [rollback] - %s' % web.ctx.orm)
        raise

