import akiyoshi

class PluginService:

    def getRrd(self, module="rrd"):
        if akiyoshi.plugins.has_key(module) is False:
            return "error"

        return akiyoshi.plugins[module]["self"]

    def getRrdType(self, category, prefix="-", module="rrd"):
        idx = category.find(prefix)
        if idx <= 0:
            return "ERROR"

        if akiyoshi.plugins.has_key(module) is False:
            return "error"

        if akiyoshi.plugins[module].has_key(category[:idx]) is False:
            return "error"

        return akiyoshi.plugins[module][category[:idx]]


pluginService = PluginService()
