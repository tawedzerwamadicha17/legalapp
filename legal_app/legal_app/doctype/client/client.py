import frappe
from frappe.model.document import Document

class Client(Document):
    def validate(self):
        self.set_full_name()
        self.validate_contact_info()
    
    def set_full_name(self):
        if self.first_name and self.last_name:
            self.full_name = f"{self.first_name} {self.last_name}"
        elif self.first_name:
            self.full_name = self.first_name
        elif self.organization_name:
            self.full_name = self.organization_name
    
    def validate_contact_info(self):
        if not self.email and not self.mobile_no and not self.phone:
            frappe.throw("At least one contact method (Email, Mobile, or Phone) is required")
    
    def after_insert(self):
        self.create_user_if_not_exists()
    
    def create_user_if_not_exists(self):
        if self.email and not frappe.db.exists("User", self.email):
            user = frappe.get_doc({
                "doctype": "User",
                "email": self.email,
                "first_name": self.first_name,
                "last_name": self.last_name,
                "user_type": "Website User"
            })
            user.insert(ignore_permissions=True)

@frappe.whitelist()
def get_client_cases(client_name):
    cases = frappe.get_all("Legal Case", 
        filters={"client": client_name},
        fields=["name", "case_title", "status", "next_hearing_date"]
    )
    return cases
