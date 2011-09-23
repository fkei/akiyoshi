#!/usr/bin/env python
# -*- coding: utf-8 -*-

from db.model.notebook import Notebook

class NotebookAccess:
    def findby1(self, session, id):
        return session.query(Notebook).filter(Notebook.id == id).first()

    def add(self, session, notebook):
        return session.add(notebook)

    def delete(self, session, notebook):
        return session.delete(notebook)

    def merge(self, session, notebook):
        return session.merge(notebook)

notebookAccess = NotebookAccess()

