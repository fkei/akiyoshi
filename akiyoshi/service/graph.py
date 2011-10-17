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
                regx = "^("+category+")"
                if re.search(regx, f):
                    link = {}
                    link["url"] = "%s/%s/%s" % (prefix, host, f)
                    link["name"] = f
                    link["type"] = []
                    for t in os.listdir("%s/%s" % (hostdir, f)):
                        link["type"].append(os.path.splitext(t)[0].replace(category+"-", ""))

                    links.append(link)

            data["links"] = links
            data["extensions"] = extensions
            ret.append(data)

        return ret

graphService = GraphService()
