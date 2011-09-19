from db.model.node import Node
from db.access.tag import tagAccess

class TagService:

    def findbyCategory(self, orm, dir, category):
        nodes = tagAccess.findbyCategory(orm, category)
        return nodes

tagService = TagService()
