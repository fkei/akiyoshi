import logging

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, mapper, SessionExtension, scoped_session
from sqlalchemy.pool import SingletonThreadPool, QueuePool

import akiyoshi

import mapper

#: SQLAlchemy#Engine
__engine = None

#: SQLAlchemy#MetaData
__metadata = None

def get_engine():
    """
    """
    global __engine

    if __engine is None:
        echo = True
        echo_pool = True

        dbtype = akiyoshi.config.database["type"]
        if dbtype == "sqlite":
            engine = create_engine(akiyoshi.config.database["bind"],
                                   encoding="utf-8",
                                   convert_unicode=True,
                                   echo=echo,
                                   echo_pool=echo_pool
                                   )
        else:
            engine = create_engine(akiyoshi.config.database["bind"],
                                   encoding="utf-8",
                                   convert_unicode=True,
                                   poolclass=QueuePool,
                                   pool_size=int(akiyoshi.config.database["pool_size"]),
                                   max_overflow=int(akiyoshi.config.database["max_overflow"]),
                                   echo=echo,
                                   echo_pool=echo_pool
                                   )

        akiyoshi.log.debug("engine name=%s, pool class=%s"
                           % (engine.name, engine.pool.__class__))

        # Metadata mapping!!
        __engine = engine
        get_metadata()

    return __engine

def get_metadata():
    """
    """
    global __engine
    global __metadata
    if __engine is None:
        __engine = get_engine()

    if __metadata is None:
        __metadata = MetaData(__engine)
        mapper.reload_mappers(__metadata)
    
    # TODO develop
    #import pdb; pdb.set_trace()
    #__metadata.create_all()

    return __metadata

def get_session():
    return scoped_session(
        sessionmaker(bind=get_engine(), autoflush=False))
