import os
import re
import os.path

from service.node import nodeService
from db.access.tag import tagAccess

class GraphService:

    def getGraphLinks(self, orm, basedir, target, category, type, extensions=[".png", ".dat"], prefix="/graph"):
        ret = []
        _tags = []

        if type == "group" or type == "compare":
            hosts = target.split(",")
            if 1 < len(hosts):
                _tags = hosts

        elif type == "tag":
            # tag
            tags = tagAccess.findby1name(orm, target)
            for tag in tags.nodes:
                _tags.append(tag.host)
        else:
            # host
            _tags.append(target)

        for host in _tags:
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

        if type != "compare":
            return ret
        
        return convertCompare(ret, target, prefix)

def convertCompare(ret, target, prefix):
    compare = {}
    compare["extensions"] = []
    compare["name"] = target
    compare["links"] = []
        
    links = {}
    for data in ret:
        compare["extensions"] = compare["extensions"] + data["extensions"]
        for link in data["links"]:
            name = link["name"]
            if links.has_key(name) is False:
                links[name] = {
                    "name": "",
                    "url": "",
                    "type": []
                    }
                
            # type
            links[name]["type"] = links[name]["type"] + link["type"]
            
            # url
            links[name]["url"] = "%s/%s/%s" \
                                 % (prefix, target, name)
            # name
            links[name]["name"] = name
            
    for data in links:
        links[data]["type"] = list(set(links[data]["type"]))
        compare["links"].append(links[data])

    compare["extensions"] = list(set(compare["extensions"]))

    return [compare, ]
    
graphService = GraphService()
