$.akiyoshi.addHandler("node", new function() {
	this.info = function(category, callback) {
        category = category || "";
		$.akiyoshi.ajax.async({
			type: "GET",        
			url: "/node/" + category
		})
		.success(function(data) {
			callback(null, data);
		})
		.error(function(jqXHR, textStatus, errorThrown) {
			callback(textStatus);
		})
		.end()
		;
	};

    this.save = function(form_id, callback) {
        $.akiyoshi.ajax.async({
            type: "POST",
            url: "/node",
            data: $("#"+form_id).serialize(),
            dataType: "html"
        })
		.success(function(data) {
            debugger;
			callback(null, data);
		})
		.error(function(jqXHR, textStatus, errorThrown) {
            debugger;
			callback(textStatus);
		})
		.end()
		;
    };

    this.postModal = function(host, callback) {
        $("#modal")
        .empty()
        .tag("div", {class: "modal-header"})
            .tag("a", {href: "#", class: "close"}).text("×").gat()
            .tag("h3").text("Server Save").gat()
        .gat()
        .tag("div", {class: "modal-body"})
            .tag("form", {id:"postModalForm"})
                .tag("div", {class: "clearfix"})
                    .tag("label", {"for": "xlInput"}).text("Host name").gat()
                    .tag("div", {class: "input"})
                        .tag("input", {type: "text", id: "host", name: "host", size: "30", value: host || "", class: "xlarge"}).gat()
                    .gat()
                .gat()
                .tag("div", {class: "clearfix"})
                    .tag("label", {"for": "normalSelect"}).text("Tag Category").gat()
                    .tag("div", {class: "input"})
                        .tag("select", {name: "category", id: "category"})
                            .tag("option").text("server").gat()
                        .gat()
                    .gat()
                .gat()
                .tag("div", {class: "clearfix"})
                    .tag("label", {"for": "xlInput"}).text("Tags").gat()
                    .tag("div", {class: "input"})
                        .tag("input", {type: "text", id: "tags", name: "tags", size: "60", value: "", class: "xlarge"}).gat()
                        .tag("span", {class: "help-block"}).text("The grouping of servers. Comma separated.").gat()
                    .gat()
                .gat()
                .tag("div", {class: "clearfix"})
                    .tag("label", {"for": "xlInput"}).text("NoteBook").gat()
                    .tag("div", {class: "input"})
                        .tag("textarea", {type: "text", id: "notebook", name: "notebook", value: "", cols: "30", rows: "3", class: "xlarge"}).gat()
                        .tag("span", {class: "help-block"}).text("Please leave a note like.").gat()
                    .gat()
                .gat()
            .gat()
        .gat()
        .tag("div", {class: "modal-footer"})
            .tag("button", {class: "btn primary small"}).text("Save").click(function() {
                $.akiyoshi.node.save("postModalForm", function() {

                    //$("#modal").modal('hide'); // modal hide.
                });
                
            }).gat()
            .tag("button", {class: "btn close small", style: "margin: 0px;"}).text("Cancel").gat()
        .gat()
        ;
        if (callback) {
            callback();
        }
    };

	this.list = function(id, callback) {
		$.akiyoshi.ajax.async({
			type: "GET",
			url: "/node"
		})
		.success(function(data) {
			callback(null, data);
		})
		.error(function(jqXHR, textStatus, errorThrown) {
			callback(textStatus);
		})
		.end()
		;
	};
});
