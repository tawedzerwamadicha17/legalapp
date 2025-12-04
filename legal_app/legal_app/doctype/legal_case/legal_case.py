import frappe
from frappe.model.document import Document

class LegalCase(Document):
    def validate(self):
        self.set_case_title()
        self.validate_dates()
        self.calculate_days_remaining()
    
    def set_case_title(self):
        if not self.case_title:
            self.case_title = f"{self.case_type} - {self.party_names}"
    
    def validate_dates(self):
        if self.filing_date and self.closure_date:
            if self.closure_date < self.filing_date:
                frappe.throw("Closure Date cannot be before Filing Date")
    
    def calculate_days_remaining(self):
        if self.next_hearing_date:
            from frappe.utils import nowdate
            from datetime import datetime
            
            next_hearing = datetime.strptime(self.next_hearing_date, "%Y-%m-%d")
            today = datetime.strptime(nowdate(), "%Y-%m-%d")
            days_remaining = (next_hearing - today).days
            self.days_until_hearing = days_remaining
    
    def before_save(self):
        self.update_case_status()
    
    def update_case_status(self):
        if not self.status:
            self.status = "Open"
        
        if self.closure_date:
            self.status = "Closed"

@frappe.whitelist()
def get_case_details(case_name):
    case = frappe.get_doc("Legal Case", case_name)
    return {
        "case_title": case.case_title,
        "status": case.status,
        "next_hearing": case.next_hearing_date,
        "client": case.client
    }
