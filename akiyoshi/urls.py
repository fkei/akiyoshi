import os
import re

def load():
    ret = []
    for controller in os.listdir('./controller'):
        if re.search('.py$', controller):
            name = controller[0: controller.index('.')]
            if name == '__init__':
                continue
            mod = __import__('controller.' + name)
            method = getattr(mod, name)
            ret += method.urls

    return ret

if __name__ == '__main__':
    load()
