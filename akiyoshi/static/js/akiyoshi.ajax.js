$.akiyoshi.addHandler("ajax", new function() {

    this.init = function() {
        // define
        $.ajaxSetup({
            //timeout: 30, // TODO
            beforeSend: this._ajax_beforeSend,
            complete: this._ajax_complete,
            error: this._ajax_error,
            //cache: false,
            async: true,
            dataType: "json",
            statusCode: {
				404: function() {
					alert("404");
				}
			}
        });
    };

    this.async = function(ajaxOptions) {
        var ret =  (function(ajaxOptions) {
            this.ajax_options = ajaxOptions || {};
            this.options = {};

            this.accepts = function(map) {
                this.options["accepts"] = map;
                return this;
            },
            this.async = function(bool) {
                this.options["async"] = bool;
                return this;
            },
            this.beforeSend = function(fn) {
                this.options["beforeSend"] = fn;
                return this;
            },
            this.cache = function(bool) {
                this.options["cache"] = cache;
                return this;
            },
            this.complete = function(fn/**, arr**/) {
                this.options["complete"] = fn;
                return this;
            },
            this.contents = function(map) {
                this.options["content"] = map;
                return this;
            },
            this.contentType = function(str) {
                this.options["contentType"] = str;
                return this;
            },
            this.context = function(obj) {
                this.options["context"] = obj;
                return this;
            },
            this.converters = function(map) {
                this.options["converters"] = map;
                return this;
            },
            //this.crossDomain = function() {},
            this.data = function(obj/**, str**/) {
                this.options["data"] = obj;
                return this;
            },
            this.dataFilter = function(fn) {
                this.options["dataFilter"] = fn;
                return this;
            },
            this.dataType = function(str) {
                this.options["dataType"] = str;
                return this;
            },
            this.error = function(fn) {
                this.options["error"] = fn;
                return this;
            },
            this.global = function(bool) {
                this.options["global"] = bool;
                return this;
            },
            this.headers = function(map) {
                this.options["headers"] = map;
                return this;
            },
            this.ifModified = function(bool) {
                this.options["ifModified"] = bool;
                return this;
            },
            this.isLocal = function(bool) {
                this.options["isLocal"] = bool;
                return this;
            },
            this.jsonp = function(str) {
                this.options["jsonp"] = str;
                return this;
            },
            //this.jsonpCallback = function(str, fn) {},
            this.mimeType = function(str) {
                this.options["mimeType"] = str;
                return this;
            },
            this.password = function(str) {
                this.options["password"] = str;
                return this;
            },
            this.processData = function(str) {
                this.options["processData"] = str;
                return this;
            },
            this.scriptCharset = function(str) {
                this.options["scriptCharset"] = str;
                return this;
            },
            this.statusCode = function(map) {
                this.options["statusCode"] = map;
                return this;
            },
            this.success = function(fn/**, arr**/) {
                this.options["success"] = fn;
                return this;
            },
            this.timeout = function(number) {
                this.options["timeout"] = number;
                return this;
            },
            this.traditional = function(bool) {
                this.options["traditional"] = bool;
                return this;
            },
            this.type = function(str) {
                this.options["type"] = str;
                return this;
            },
            this.url = function(str) {
                this.options["url"] = str;
                return this;
            },
            this.xhr = function(fn) {
                this.options["xhr"] = fn;
                return this;
            },
            this.xhrFields = function(map) {
                this.options["xhrFields"] = map;
                return this;
            },
            this.end = function() {
                for (var key in this.options) {
	                this.ajax_options[key] = this.options[key];
                }
                return $.ajax(this.ajax_options);
            }
        });
        return new ret(ajaxOptions);
    };

    this._ajax_beforeSend = function(jqXHR, settings) {
        // TODO: beforre request
    };

    this._ajax_complete = function(jqXHR, textStatus) {
        // TODO: response process
        if(XMLHttpRequest.status === "202") {
            // TODO: HTTP return code : Accepted
        } else if(XMLHttpRequest.status === "204") {
            // TODO: HTTP return code : No Content
        }
    };
    this._ajax_error = function (jqXHR, textStatus, errorThrown) {
        var content = jQuery.parseJSON(jqXHR.responseText);
        // TODO error handring.
        alert(content.error.name + " : " + content.error.message);

        if(jqXHR.status === "400") {
            // TODO: HTTP return code : Bad Request
        } else if (jqXHR.status === "404") {
            // TODO: HTTP return code : Not Found
        } else if (jqXHR.status === "405") {
            // TODO: HTTP return code : Method Not Allowed
        } else if (jqXHR.status === "409") {
            // TODO: HTTP return code : Conflict
        } else {
            // TODO: HTTP return code : Illegal Error
        }
    };
});

