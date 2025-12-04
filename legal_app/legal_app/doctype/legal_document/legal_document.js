frappe.ui.form.on('Legal Document', {
    refresh: function(frm) {
        // Make the attachment field mandatory
        frm.toggle_reqd('attachment', true);
    },

    linked_case: function(frm) {
        // Auto-fill document title from case
        if (frm.doc.linked_case && !frm.doc.document_title) {
            frappe.model.with_doc('Legal Case', frm.doc.linked_case, function() {
                const legal_case = frappe.model.get_doc('Legal Case', frm.doc.linked_case);
                frm.set_value('document_title', `Document for ${legal_case.case_title}`);
            });
        }
    }
});
