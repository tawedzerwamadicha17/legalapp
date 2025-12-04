import frappe
from frappe.utils import nowdate, add_days

def send_hearing_reminders():
    """Send reminders for upcoming hearings"""
    tomorrow = add_days(nowdate(), 1)
    
    upcoming_hearings = frappe.get_all("Hearing", 
        filters={
            "hearing_date": tomorrow,
            "status": ["!=", "Cancelled"]
        },
        fields=["name", "legal_case", "hearing_date", "title"]
    )
    
    for hearing in upcoming_hearings:
        # Get case details
        case = frappe.get_doc("Legal Case", hearing.legal_case)
        
        # Send email to assigned counsel
        if case.counsel_email:
            subject = f"Hearing Reminder: {case.case_title}"
            message = f"""
            Reminder: You have a hearing scheduled for tomorrow.
            
            Case: {case.case_title}
            Hearing: {hearing.title}
            Date: {hearing.hearing_date}
            
            Please prepare accordingly.
            """
            
            frappe.sendmail(
                recipients=[case.counsel_email],
                subject=subject,
                message=message
            )
