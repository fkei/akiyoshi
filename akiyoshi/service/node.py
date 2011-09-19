import os
import os.path

from db.model.node import Node
from db.model.notebook import NoteBook
from db.model.tag import Tag

from db.access.tag import tagAccess
from db.access.node import nodeAccess

class NodeService:

    def fsnodes(self, directory):
        if os.path.isdir(directory) is False:
            return []
        else:
            ret = []
            categorys = os.listdir(directory)
            categorys.sort()
            return categorys

    def nodes(self, orm, dir):
        controlNodes = orm.query(Node).all()
        fsNodes = self.fsnodes(dir)
        return (controlNodes, fsNodes)

    def nodeGroup(self, orm, dir, category):
        tag = tagAccess.findby1name(orm, category)

        controlNodes = []
        fsNodes = []
        for node in tag.nodes:
            controlNodes.append(node)
            if os.path.isdir("%s/%s" % (dir, node.host)):
                fsNodes.append(node.utf8("host"))

        return (controlNodes, fsNodes)

    def save(self, orm, me, host, notebook, categorys, tags):
        # tags -> listdir
        _tags = []
        for y in [x.strip() for x in tags.split(',') if x]:
            _tags.append(y)

        otags = None
        if _tags:
            _tags = sorted(_tags)
            otags = []
            for x in _tags:
                if tagAccess.countby1name(orm, x) == 0:
                    otags.append(Tag(x, categorys)) # New
                else:
                    otags.append(tagAccess.findby1name(orm, x)) # reuse

        notebook = NoteBook(notebook)
        node = Node(me, me, host, notebook, otags)
        return nodeAccess.merge(orm, node)

nodeService = NodeService()
