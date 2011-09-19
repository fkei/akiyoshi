#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db.model.tag import Tag

class TagAccess:
    def findby1(self, session, id):
        return session.query(Tag).filter(Tag.id == id).first()

    def countby1name(self, session, name):
        return session.query(Tag).filter(Tag.name == name).count()

    def findby1name(self, session, name):

        if type(name) == unicode:
            name = str(name)

        return session.query(Tag).filter(Tag.name == name).first()

    def findbyCategory(self, session, category):
        return session.query(Tag).filter(Tag.category == category).all()

    def save(self, session, tag):
        return session.save(tag)

    def update(self, session, tag):
        return session.update(tag)

    def delete(self, session, tag):
        return session.delete(tag)

    def merge(self, session, tag):
        return session.merge(tag)

tagAccess = TagAccess()

