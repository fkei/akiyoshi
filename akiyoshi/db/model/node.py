#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy.orm import mapper, clear_mappers, relation, relationship, backref

from __init__ import Model
from user import User
from notebook import NoteBook
from tag import Tag

def get_node(metadata, now):
    return sqlalchemy.Table('node', metadata,
                            sqlalchemy.Column('id', sqlalchemy.Integer,
                                              primary_key=True,
                                              autoincrement=True,
                                              ),
                            sqlalchemy.Column('notebook_id', sqlalchemy.Integer,
                                              sqlalchemy.ForeignKey('notebook.id'),
                                              ),
                            sqlalchemy.Column('host', sqlalchemy.String(256),
                                              nullable=True,
                                              unique=True,
                                              ),
                            sqlalchemy.Column('created_user_id', sqlalchemy.Integer,
                                              sqlalchemy.ForeignKey('user.id'),
                                              ),
                            sqlalchemy.Column('modified_user_id', sqlalchemy.Integer,
                                              sqlalchemy.ForeignKey('user.id'),
                                              ),
                            sqlalchemy.Column('created', sqlalchemy.DateTime,
                                              default=now,
                                              ),
                            sqlalchemy.Column('modified', sqlalchemy.DateTime,
                                              default=now,
                                              onupdate=now,
                                              ),
                            )


class Node(Model):

    def __init__(self, created_user, modified_user, host, notebook, tags=[]):
        self.created_user = created_user
        self.modified_user = modified_user
        self.host = host
        self.node = node
        self.notebook = notebook
        self.tags = tags

    def json(self):
        ret = {}
        ret["id"] = self.id
        ret["notebook"] = self.notebook()
        ret["host"] = self.host
        ret["created_user"] = self.created_user
        ret["modified_user"] = self.modified_user
        ret["tags"] = []
        if self.tags:
            for x in self.tags:
                ret["tags"].append(x.json())

        return ret

    def __repr__(self):
        return "Node<%s>" % (self.host)

def reload_mapper(metadata, now):
    t_node = get_node(metadata, now)

    t_node2tag = metadata.tables["node2tag"]
    t_user = metadata.tables["user"]

    mapper(Node, t_node, properties={
        "notebook": relation(NoteBook),
        "created_user": relation(User,primaryjoin=t_node.c.created_user_id==t_user.c.id),
        "modified_user": relation(User, primaryjoin=t_node.c.modified_user_id==t_user.c.id),
        "tags": relation(Tag, secondary=t_node2tag, backref="node")
    })

