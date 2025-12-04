import frappe
from frappe.utils import nowdate, add_months

def archive_closed_cases():
    """Archive cases closed more than 6 months ago"""
    six_months_ago = add_months(nowdate(), -6)
    
    closed_cases = frappe.get_all("Legal Case",
        filters={
            "status": "Closed",
            "closure_date": ["<", six_months_ago]
        },
        fields=["name"]
    )
    
    for case in closed_cases:
        # Archive the case
        frappe.db.set_value("Legal Case", case.name, "archived", 1)
        frappe.logger().info(f"Archived case: {case.name}")
