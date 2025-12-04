from frappe import _

def get_data():
    return [
        # Module Configuration
        {
            "label": _("Documents"),
            "icon": "octicon octicon-file",
            "items": [
                {
                    "type": "doctype",
                    "name": "Legal Case",
                    "label": _("Legal Case"),
                    "description": _("Legal case details and tracking"),
                },
                {
                    "type": "doctype",
                    "name": "Client",
                    "label": _("Client"),
                    "description": _("Client information and details"),
                },
                {
                    "type": "doctype",
                    "name": "Legal Document",
                    "label": _("Legal Document"),
                    "description": _("Legal documents and files"),
                },
                {
                    "type": "doctype",
                    "name": "Hearing",
                    "label": _("Hearing"),
                    "description": _("Court hearing schedule and details"),
                }
            ]
        },
        {
            "label": _("Masters"),
            "icon": "octicon octicon-book",
            "items": [
                {
                    "type": "doctype",
                    "name": "Court",
                    "label": _("Court"),
                    "description": _("Court information"),
                },
                {
                    "type": "doctype",
                    "name": "Judge",
                    "label": _("Judge"),
                    "description": _("Judge information"),
                },
                {
                    "type": "doctype",
                    "name": "Case Type",
                    "label": _("Case Type"),
                    "description": _("Types of legal cases"),
                }
            ]
        },
        {
            "label": _("Setup"),
            "icon": "octicon octicon-gear",
            "items": [
                {
                    "type": "doctype",
                    "name": "Legal App Settings",
                    "label": _("Legal App Settings"),
                    "description": _("Global settings for Legal App"),
                }
            ]
        }
    ]
