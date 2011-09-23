$.akiyoshi.addHandler("bootstrap", new function() {
    this.init = function() {
        /*
        var options = {
            animate: true,
            delayIn: 0,
            delayOut: 0,
            fallback: "",
            placement: "right",
            html: true,
            live: false,
            offset: 0,
            title: "title",
            content: "data-content",
            trigger: "hover"
        };
        $().popover(options);
        */
    };
    
	this.popovers = function(elem, title, data, options) {
        elem.attr("title", title);
        elem.attr("data-content", data);
        elem.popover(options);
        return this;
    };
});