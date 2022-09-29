// Copyright (c) 2022, KodeIT and contributors
// For license information, please see license.txt

frappe.ui.form.on('Visitor', {
	// refresh: function(frm) {

	// }
	 frm.set_query("vistor", function() {
        return {
            "filters": {
                "visitor_name": "visitor_name",
            }
        };
    });

});

