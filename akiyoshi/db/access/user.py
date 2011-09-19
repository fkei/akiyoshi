# -*- coding: utf-8 -*-

class UserAccess:
    def findby1(self, session, id):
        return session.query(User).filter(User.id == id).first()

    def findby1email(self, session, email):
        return session.query(User).filter(User.email == email).first()

    def save(self, session, user):
        session.save(user)

    def update(self, session, user):
            session.update(user)

    def delete(self, session, user):
        session.delete(user)

    def merge(self, session, user):
        session.merge(user)

userAccess = UserAccess()
