# -*- coding: utf-8 -*-

from db.model.node import Node

class NodeAccess:
    def findby1(self, session, id):
        return session.query(Node).filter(Node.id == id).first()

    def findbyhost(self, session, host):
        return session.query(Node).filter(Node.host == host).first()

    def add(self, session, node):
        return session.add(node)

    def delete(self, session, node):
        return session.delete(node)

    def merge(self, session, node):
        return session.merge(node)

nodeAccess = NodeAccess()
