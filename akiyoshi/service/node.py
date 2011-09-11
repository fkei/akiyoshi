import os
import os.path

class NodeService():

    def list(self, directory, host=None, category=None):
        target = directory
        if host:
            target = "%s/%s" % (target, host)

        if category:
            target = "%s/%s" % (target, category)

        if os.path.isdir(target) is False:
            return []
        else:
            return os.listdir(target)

nodeService = NodeService()
