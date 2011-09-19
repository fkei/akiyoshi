#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy.orm import mapper, clear_mappers

from __init__ import Model

def get_notebook(metadata, now):
    return sqlalchemy.Table('notebook', metadata,
                            sqlalchemy.Column('id', sqlalchemy.Integer,
                                              primary_key=True,
                                              autoincrement=True,
                                              ),
                            sqlalchemy.Column('value', sqlalchemy.Text,
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

class NoteBook(Model):
    def __init__(self, value):
        self.value = value

    def json(self):
        ret = {}
        ret["id"] = self.id
        ret["value"] = self.value
        ret["created"] = self.created
        ret["modified"] = self.modified
        return ret

    def __repr__(self):
        return "NoteBook<%s>" % (self.id)

def reload_mapper(metadata, now):
    t_notebook = get_notebook(metadata, now)
    mapper(NoteBook, t_notebook)
