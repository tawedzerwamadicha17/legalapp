import frappe
from frappe.utils import get_url

def on_case_update(doc, method=None):
    """Triggered when Legal Case is updated"""
    if doc.has_value_changed('status'):
        create_case_status_activity(doc)
    
    if doc.has_value_changed('next_hearing_date'):
        notify_hearing_date_change(doc)

def send_case_creation_email(doc, method=None):
    """Send email when new case is created"""
    if doc.client and doc.email:
        subject = f"New Case Created: {doc.case_title}"
        message = f"""
        Dear Client,
        
        A new case has been created for you:
        
        Case Title: {doc.case_title}
        Case Number: {doc.case_number}
        Filing Date: {doc.filing_date}
        
        You can view your case details at: {get_url()}/app/legal-case/{doc.name}
        
        Best regards,
        Legal Team
        """
        
        frappe.sendmail(
            recipients=[doc.email],
            subject=subject,
            message=message
        )

def create_case_status_activity(doc):
    """Create system activity when case status changes"""
    frappe.get_doc({
        "doctype": "Comment",
        "comment_type": "Info",
        "reference_doctype": "Legal Case",
        "reference_name": doc.name,
        "content": f"Case status changed from {doc.get_doc_before_save().status} to {doc.status}"
    }).insert(ignore_permissions=True)

def notify_hearing_date_change(doc):
    """Notify when hearing date changes"""
    if doc.next_hearing_date:
        # Create calendar event or send notification
        pass
