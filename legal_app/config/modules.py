from frappe import _

def get_data():
    return [
        {
            "module_name": "Legal App",
            "category": "Modules",
            "label": _("Legal App"),
            "color": "#3498db",
            "icon": "octicon octicon-law",
            "type": "module",
            "disable_after_onboard": 0,
            "description": "Legal case and document management system.",
            "onboard_present": 1
        }
    ]
