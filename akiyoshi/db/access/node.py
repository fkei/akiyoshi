# -*- coding: utf-8 -*-

class NodeAccess:
    def findby1(self, session, id):
        return session.query(Node).filter(Node.id == id).first()

    def save(self, session, node):
        return session.save(node)

    def update(self, session, node):
        return session.update(node)

    def delete(self, session, node):
        return session.delete(node)

    def merge(self, session, node):
        return session.merge(node)

nodeAccess = NodeAccess()
