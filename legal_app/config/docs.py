"""
Configuration for documentation
"""

source_link = "https://github.com/your-username/legal_app"
headline = "Legal Case Management System"
sub_heading = "Comprehensive legal case and document management"
long_description = """# Legal App

A comprehensive legal management system for law firms and legal departments.

## Features

- Case Management
- Document Management
- Client Management
- Hearing Schedule Management
- Legal Document Templates
- Time Tracking and Billing
- Court and Judge Database
- Legal Calendar

## Modules

### Case Management
Track all legal cases with detailed information including case type, status, priority, and associated documents.

### Client Management
Manage client information, contact details, and case history.

### Document Management
Store and organize legal documents with version control and access permissions.

### Hearing Management
Schedule and track court hearings with reminders and calendar integration.
"""

def get_context(context):
    context.brand_html = "Legal App"
