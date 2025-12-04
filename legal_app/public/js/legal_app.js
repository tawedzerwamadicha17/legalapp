// Legal App Custom JavaScript

frappe.ready(function() {
    // Initialize legal app features
    initializeCaseDashboard();
    initializeHearingCalendar();
});

function initializeCaseDashboard() {
    // Add custom behavior to case dashboard
    $('.legal-case-card').click(function() {
        const caseName = $(this).data('case-name');
        frappe.set_route('Form', 'Legal Case', caseName);
    });
}

function initializeHearingCalendar() {
    // Initialize hearing calendar if on calendar page
    if ($('.hearing-calendar').length) {
        loadHearingCalendar();
    }
}

function loadHearingCalendar() {
    frappe.call({
        method: 'legal_app.utils.calendar_utils.get_hearing_events',
        callback: function(response) {
            if (response.message) {
                renderHearingCalendar(response.message);
            }
        }
    });
}

function renderHearingCalendar(events) {
    // Implement calendar rendering logic here
    console.log('Rendering hearing events:', events);
}

// Custom form scripts for Legal Case
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
    },
    
    client: function(frm) {
        // Auto-fill some fields based on client
        if (frm.doc.client) {
            frappe.model.with_doc('Client', frm.doc.client, function() {
                const client = frappe.model.get_doc('Client', frm.doc.client);
                // You can auto-fill fields here if needed
            });
        }
    }
});

// Custom form scripts for Client
frappe.ui.form.on('Client', {
    validate: function(frm) {
        // Additional client validation
        if (!frm.doc.email && !frm.doc.mobile_no) {
            frappe.msgprint(__('Please provide at least one contact method'));
            frappe.validated = false;
        }
    }
});

// Utility functions
function calculateDaysUntilHearing(hearingDate) {
    const today = new Date();
    const hearing = new Date(hearingDate);
    const diffTime = hearing - today;
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    return diffDays;
}

function formatCaseNumber(caseType, year, sequence) {
    return `${caseType}/${year}/${sequence.toString().padStart(4, '0')}`;
}
