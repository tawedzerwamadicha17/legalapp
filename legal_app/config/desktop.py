from frappe import _

def get_data():
    return [
        {
            "module_name": "Legal App",
            "color": "blue",
            "icon": "octicon octicon-law",
            "type": "module",
            "label": _("Legal App")
        },
        {
            "module_name": "Case Management",
            "color": "green",
            "icon": "octicon octicon-briefcase",
            "type": "module",
            "label": _("Case Management"),
            "link": "modules/Case Management"
        },
        {
            "module_name": "Client Management",
            "color": "orange",
            "icon": "octicon octicon-organization",
            "type": "module",
            "label": _("Client Management"),
            "link": "modules/Client Management"
        },
        {
            "module_name": "Document Management",
            "color": "red",
            "icon": "octicon octicon-file",
            "type": "module",
            "label": _("Document Management"),
            "link": "modules/Document Management"
        }
    ]
