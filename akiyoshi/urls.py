import os
import re
import sys

def load():
    ret = []
    for controller in os.listdir("./controller"):
        if re.search(".py$", controller) and not re.search("^#", controller):
            name = controller[0: controller.index(".")]
            if name == "__init__":
                continue
            try:
                mod = __import__("controller." + name)
                method = getattr(mod, name)
                ret += method.urls
                print >>sys.stdout, "[INFO] register conntroller. %s" % (name)
            except Exception, e:
                print >>sys.stderr, "[ERROR] no register conntroller. %s#%s" % (controller, name)
                raise e

    return ret

if __name__ == "__main__":
    load()
