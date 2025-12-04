import frappe
from frappe.model.document import Document

class LegalDocument(Document):
    def before_save(self):
        self.set_document_title()
        self.update_linked_case()
    
    def set_document_title(self):
        if not self.document_title and self.document_name:
            self.document_title = self.document_name
    
    def update_linked_case(self):
        if self.linked_case and self.is_new():
            # Update case's last document date
            frappe.db.set_value("Legal Case", self.linked_case, "last_document_date", self.creation)
