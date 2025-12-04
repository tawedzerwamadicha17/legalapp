import frappe

def validate_hearing_date(doc, method=None):
    """Validate hearing date is not in past"""
    from frappe.utils import get_datetime, now_datetime
    
    if get_datetime(doc.hearing_date) < now_datetime():
        frappe.throw("Cannot schedule hearing in the past")

def update_case_status(doc, method=None):
    """Update linked case status based on hearing"""
    if doc.legal_case and doc.status == "Completed":
        # Update case status if hearing completed
        frappe.db.set_value("Legal Case", doc.legal_case, "last_hearing_date", doc.hearing_date)
