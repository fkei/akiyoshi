#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy.orm import mapper, clear_mappers, relation, relationship, backref

from __init__ import Model

def get_tag(metadata, now):
    return sqlalchemy.Table('tag', metadata,
                            sqlalchemy.Column('id', sqlalchemy.Integer,
                                              primary_key=True,
                                              autoincrement=True,
                                              ),
                            sqlalchemy.Column('category', sqlalchemy.String(24),
                                              nullable=False,
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
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def jsonall(self):
        ret = {}
        ret["id"] = self.id
        ret["category"] = self.category
        ret["name"] = self.name
        ret["created"] = self.created
        ret["modified"] = self.modified

        return ret

    def json(self):
        ret = {}
        #ret["id"] = self.id
        ret["category"] = self.category
        ret["name"] = self.name
        #ret["created"] = self.created
        #ret["modified"] = self.modified

        return ret

    def __repr__(self):
        return "Tag<'%s', '%s'>" % (self.category, self.name)

def reload_mapper(metadata, now):
    t_tag = get_tag(metadata, now)
    t_node2tag = metadata.tables["node2tag"]
    from node import Node
    mapper(Tag, t_tag, properties={
        "nodes": relation(Node, secondary=t_node2tag, backref="tag")
    })

