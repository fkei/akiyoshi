import os
import os.path

from db.access.tag import tagAccess
from db.access.node import nodeAccess

class MonitorService:


    def list(self, orm, directory, host, prefix):
        ret = {
            "node": {},
            "all": []
            }

        if os.path.isdir(directory) is False:
            return ret
        else:
            node = nodeAccess.findbyhost(orm, host)

            if node is None:
                return ret

            target = "%s/%s" % (directory, host)
            if os.path.isdir(target) is False:
                return ret

            ret["node"][host] = {}
            categorys = os.listdir(target)

            if prefix is False:
                categorys.sort()
                return categorys

            plist = []
            for category in categorys:
                idx = category.find("-")
                if idx != -1:
                    plist.append(category[:idx])
                else:
                    plist.append(category)

            plist = list(set(plist))
            plist.sort()
            ret["node"][host]["category"] = plist
            ret["all"] = plist

        return ret

    def groupList(self, directory, hosts, prefix):
        ret = {
            "node": {},
            "all": []
            }

        if os.path.isdir(directory) is False:
            return ret

        for host in hosts:
            target = "%s/%s" % (directory, host)
            ret["node"][host] = {}

            if os.path.isdir(target) is False:
                continue

            categorys = os.listdir(target)

            if prefix is False:
                categorys.sort()
                ret["node"][host]["category"] = category
            else:
                alist = []
                plist = []

                for category in categorys:
                    idx = category.find("-")
                    if idx != -1:
                        plist.append(category[:idx])
                    else:
                        plist.append(category)

                plist = list(set(plist))
                plist.sort()
                ret["node"][host]["category"] = plist
                alist = alist+plist
                alist = list(set(alist))
                alist.sort()
                ret["all"] = alist

        return ret

    def compareList(self, directory, hosts, prefix):
        ret = {
            "node": {},
            "all": []
            }

        if os.path.isdir(directory) is False:
            return ret

        for host in hosts:
            target = "%s/%s" % (directory, host)
            ret["node"][host] = {}

            if os.path.isdir(target) is False:
                continue

            categorys = os.listdir(target)

            if prefix is False:
                categorys.sort()
                ret["node"][host]["category"] = category
            else:
                alist = []
                plist = []

                for category in categorys:
                    idx = category.find("-")
                    if idx != -1:
                        plist.append(category[:idx])
                    else:
                        plist.append(category)

                plist = list(set(plist))
                plist.sort()
                ret["node"][host]["category"] = plist
                alist = alist+plist
                alist = list(set(alist))
                alist.sort()
                ret["all"] = alist

        return ret

            
    def tagList(self, orm, directory, category, prefix):
        ret = {
            "node": {},
            "all": []
            }

        if os.path.isdir(directory) is False:
            return ret

        tag = tagAccess.findby1name(orm, category)

        if tag is None:
            return ret

        for node in tag.nodes:
            host = node.host
            target = "%s/%s" % (directory, host)
            ret["node"][host] = {}

            if os.path.isdir(target) is False:
                continue

            categorys = os.listdir(target)

            if prefix is False:
                categorys.sort()
                ret["node"][host]["category"] = category
            else:
                alist = []
                plist = []
                for category in categorys:
                    idx = category.find("-")
                    if idx != -1:
                        plist.append(category[:idx])
                    else:
                        plist.append(category)

                plist = list(set(plist))
                plist.sort()
                ret["node"][host]["category"] = plist
                alist = alist+plist
                alist = list(set(alist))
                alist.sort()
                ret["all"] = alist

        return ret

monitorService = MonitorService()
