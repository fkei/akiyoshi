$.akiyoshi.addHandler("util", new function() {
    this.date2str = function(date) {
        date = new Date(Number(date));

        return date.getFullYear()
            + "/"
            + this.zero((date.getMonth()+1),2)
            + "/"
            + this.zero(date.getDate(),2)
            + " "
            + this.zero(date.getHours(),2)
            + ":"
            + this.zero(date.getMinutes(),2)
            + ":"
            + this.zero(date.getSeconds(),2);
    };

    this.zero = function(num, zero) {
        var str = String(num);
        while (str.length < zero) {
            str = "0" + str;
        }
        return str;
    };
});

