import os
import os.path

class MonitorService:

    def list(self, directory, prefix=True):
        if os.path.isdir(directory) is False:
            return []
        else:

            ret = []
            categorys = os.listdir(directory)

            if prefix is False:
                categorys.sort()
                return categorys

            for category in categorys:
                idx = category.find("-")
                if idx != -1:
                    ret.append(category[:idx])
                else:
                    ret.append(category)

            ret = list(set(ret))
            ret.sort()
            return ret

monitorService = MonitorService()
