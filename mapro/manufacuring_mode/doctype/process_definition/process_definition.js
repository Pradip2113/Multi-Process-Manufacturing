// Copyright (c) 2023, Pradip and contributors
// For license information, please see license.txt

frappe.ui.form.on('Process Definition', {
	refresh: function(frm) {

	},
	setup: function (frm) {
		frm.set_query("workstation", function () {
			return {
				filters: {"department": frm.doc.department}
			}
		});
	}
});

frappe.ui.form.on('Process Item', {
	quantity(frm) {
		// your code here
		frm.call({
			method:'qtyupdate',
			doc: frm.doc,
		});
	}
})
frappe.ui.form.on('Operation Cost', {
	cost(frm) {
		// your code here
		frm.call({
			method:'qtyupdate',
			doc: frm.doc,
		});
	}
})
frappe.ui.form.on('Process Item', {
	rate(frm) {
		// your code here
		frm.call({
			method:'qtyupdate',
			doc: frm.doc,
		});
	}
})


