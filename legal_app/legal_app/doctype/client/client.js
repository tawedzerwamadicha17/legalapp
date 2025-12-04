frappe.ui.form.on('Client', {
    refresh: function(frm) {
        // Add custom button to view client cases
        if (!frm.doc.__islocal) {
            frm.add_custom_button(__('View Cases'), function() {
                frappe.set_route('list', 'Legal Case', { client: frm.doc.name });
            });
        }
    },

    client_type: function(frm) {
        // Show/hide fields based on client type
        frm.refresh();
    },

    validate: function(frm) {
        // Client-side validation
        if (!frm.doc.email && !frm.doc.mobile_no && !frm.doc.phone) {
            frappe.msgprint(__('Please provide at least one contact method (Email, Mobile, or Phone)'));
            frappe.validated = false;
        }
    },

    onload: function(frm) {
        // Set default values
        if (frm.doc.__islocal) {
            if (!frm.doc.client_type) {
                frm.set_value('client_type', 'Individual');
            }
        }
    }
});
