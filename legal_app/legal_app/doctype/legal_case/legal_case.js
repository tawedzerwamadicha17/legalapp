frappe.ui.form.on('Legal Case', {
    refresh: function(frm) {
        // Add custom button to create related hearing
        frm.add_custom_button(__('Schedule Hearing'), function() {
            frappe.new_doc('Hearing', {
                legal_case: frm.doc.name
            });
        });
        
        // Add custom button to create document
        frm.add_custom_button(__('Add Document'), function() {
            frappe.new_doc('Legal Document', {
                linked_case: frm.doc.name
            });
        });

        // Add custom button to view case timeline
        if (!frm.doc.__islocal) {
            frm.add_custom_button(__('Case Timeline'), function() {
                frappe.set_route('list', 'Hearing', { legal_case: frm.doc.name });
            });
        }
    },
    
    client: function(frm) {
        // Auto-fill party names based on client
        if (frm.doc.client) {
            frappe.model.with_doc('Client', frm.doc.client, function() {
                const client = frappe.model.get_doc('Client', frm.doc.client);
                if (client.full_name && !frm.doc.party_names) {
                    frm.set_value('party_names', client.full_name);
                }
            });
        }
    },

    next_hearing_date: function(frm) {
        // Calculate days until hearing
        if (frm.doc.next_hearing_date) {
            const today = new Date();
            const hearingDate = new Date(frm.doc.next_hearing_date);
            const diffTime = hearingDate - today;
            const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
            frm.set_value('days_until_hearing', diffDays);
        }
    },

    validate: function(frm) {
        // Additional client-side validation
        if (frm.doc.closure_date && frm.doc.filing_date) {
            if (new Date(frm.doc.closure_date) < new Date(frm.doc.filing_date)) {
                frappe.msgprint(__('Closure Date cannot be before Filing Date'));
                frappe.validated = false;
            }
        }
    }
});
