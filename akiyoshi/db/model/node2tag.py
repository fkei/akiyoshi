#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy.orm import mapper, clear_mappers

from __init__ import Model

def get_node2tag(metadata, now):
    return sqlalchemy.Table('node2tag', metadata,
                            sqlalchemy.Column('id', sqlalchemy.Integer,
                                              primary_key=True,
                                              autoincrement=True,
                                              ),
                            sqlalchemy.Column('tag_id', sqlalchemy.Integer,
                                              sqlalchemy.ForeignKey('tag.id'),
                                              ),
                            sqlalchemy.Column('node_id', sqlalchemy.Integer,
                                              sqlalchemy.ForeignKey('node.id'),
                                              ),
                            sqlalchemy.Column('created', sqlalchemy.DateTime,
                                              default=now,
                                              ),
                            sqlalchemy.Column('modified', sqlalchemy.DateTime,
                                              default=now,
                                              onupdate=now,
                                              ),
                            )

class Node2Tag(Model):
    def __init__(self, tag_id, node_id):
        self.tag_id = tag_id
        self.node_id = node_id

    def __repr__(self):
        return "Node2tag<'%d, %s, %s'>" % (self.id, self.tag_id, self.node_id)

def reload_mapper(metadata, now):
    t_node2tag = get_node2tag(metadata, now)
