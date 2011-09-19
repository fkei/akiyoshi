$.akiyoshi.addHandler("action", new function() {
    this.update = function(list, callback) {
        $("#action")
        .tagset("ul", {class: "breadcrumb"}).next(function() {
            for (var i=0; i < list.length; i++) {
                var data = list[i];
                $(this).next(function() {
                    if (list.length - 1 == i) {
                        $(this).tag("li", {class: "active"}).text(data.name).gat();
                    } else {
                        $(this)
                        .tag("a", {link:data.link}).text(data.name).click(function() {
                            
                            
                        })
                        .tag("span", {class: "divider"}).text("/").gat()
                        .gat();
                    }
                })
                    .gat()
                ;
            };
        })
        .gat()
        ;
    };
});