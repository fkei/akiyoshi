#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db.model.notebook import Notebook

class NotebookAccess:
    def findby1(self, session, id):
        return session.query(Notebook).filter(Notebook.id == id).first()

    def save(self, session, notebook):
        return session.save(notebook)

    def update(self, session, notebook):
        return session.update(notebook)

    def delete(self, session, notebook):
        return session.delete(notebook)

    def merge(self, session, notebook):
        return session.merge(notebook)

notebookAccess = NotebookAccess()

