#!/usr/bin/env python
# -*- coding: utf-8 -*-

class UserAccess:
    def findby1(self, session, id):
        return session.query(User).filter(User.id == id).first()

    def findby1email(self, session, email):
        return session.query(User).filter(User.email == email).first()

    def save(self, session, user):
        return session.save(user)

    def update(self, session, user):
        return session.update(user)

    def delete(self, session, user):
        return session.delete(user)

    def merge(self, session, user):
        return session.merge(user)

userAccess = UserAccess()
