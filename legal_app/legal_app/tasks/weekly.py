import frappe
from frappe.utils import nowdate

def generate_case_reports():
    """Generate weekly case status reports"""
    # Get all open cases
    open_cases = frappe.get_all("Legal Case",
        filters={"status": ["in", ["Open", "In Progress", "Pending"]]},
        fields=["name", "case_title", "status", "next_hearing_date", "filing_date"]
    )
    
    # Create a summary report
    report_data = {
        "total_open_cases": len(open_cases),
        "cases_by_status": {},
        "upcoming_hearings": []
    }
    
    for case in open_cases:
        # Count by status
        report_data["cases_by_status"][case.status] = report_data["cases_by_status"].get(case.status, 0) + 1
        
        # Track upcoming hearings
        if case.next_hearing_date:
            report_data["upcoming_hearings"].append({
                "case": case.case_title,
                "hearing_date": case.next_hearing_date
            })
    
    # Store report or send to managers
    frappe.logger().info(f"Weekly Case Report: {report_data}")
