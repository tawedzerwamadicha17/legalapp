frappe.ui.form.on('Hearing', {
    refresh: function(frm) {
        // Add custom buttons
        if (frm.doc.legal_case) {
            frm.add_custom_button(__('Open Case'), function() {
                frappe.set_route('Form', 'Legal Case', frm.doc.legal_case);
            });
        }
    },

    legal_case: function(frm) {
        // Auto-fill hearing details from case
        if (frm.doc.legal_case) {
            frappe.model.with_doc('Legal Case', frm.doc.legal_case, function() {
                const legal_case = frappe.model.get_doc('Legal Case', frm.doc.legal_case);
                if (legal_case.court && !frm.doc.court) {
                    frm.set_value('court', legal_case.court);
                }
                if (legal_case.judge && !frm.doc.judge) {
                    frm.set_value('judge', legal_case.judge);
                }
            });
        }
    },

    hearing_date: function(frm) {
        // Validate hearing date is not in past
        if (frm.doc.hearing_date) {
            const today = new Date();
            const hearingDate = new Date(frm.doc.hearing_date);
            if (hearingDate < today) {
                frappe.msgprint(__('Hearing date cannot be in the past'));
                frappe.validated = false;
            }
        }
    }
});
