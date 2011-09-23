import os
import re
import os.path

from service.node import nodeService
from db.access.tag import tagAccess

class GraphService:

    def getGraphLinks(self, orm, basedir, target, category, extensions=[".png", ".dat"], prefix="/graph"):
        ret = []
        tags = tagAccess.findby1name(orm, target)

        if not tags:
            tags = [target]

        for host in tags:
            data = {}
            data["name"] = host
            hostdir = "%s/%s" % (basedir, host)
            if os.path.isdir(hostdir) is False:
                continue

            links = []
            for f in os.listdir(hostdir):
                if re.search(r"^"+category+"*", f):
                    links.append("%s/%s/%s" % (prefix, host, f))

            data["links"] = links
            data["extensions"] = extensions
            ret.append(data)

        return ret

graphService = GraphService()
