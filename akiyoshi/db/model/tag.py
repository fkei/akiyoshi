#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy.orm import mapper, clear_mappers, relation

from __init__ import Model

def get_tag(metadata, now):
    return sqlalchemy.Table('tag', metadata,
                            sqlalchemy.Column('id', sqlalchemy.Integer,
                                              primary_key=True,
                                              autoincrement=True,
                                              ),
                            sqlalchemy.Column('name', sqlalchemy.String(24),
                                              nullable=False,
                                              ),
                            sqlalchemy.Column('created', sqlalchemy.DateTime,
                                              default=now,
                                              ),
                            sqlalchemy.Column('modified', sqlalchemy.DateTime,
                                              default=now,
                                              onupdate=now,
                                              ),
                            )

class Tag(Model):
    def __init__(self, name):
        self.name = name

    def get_json(self, languages):
        ret = {}
        ret["id"] = self.id
        ret["name"] = self. name
        ret["created"] = self.created.strftime(
            DEFAULT_LANGS[languages]['DATE_FORMAT'][1])
        ret["modified"] = self.modified.strftime(
            DEFAULT_LANGS[languages]['DATE_FORMAT'][1])

        return ret

    def __repr__(self):
        return "Tag<'%s'>" % (self.name)

def reload_mapper(metadata, now):
    t_tag = get_tag(metadata, now)
    mapper(Tag, t_tag, properties={})

