from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

PAGES = [
    {
        "seperator": False,
        "items": [
            {
                "title": _("Home page"),
                "icon": "home",
                "link": reverse_lazy("admin:index"),
            }
        ],
    },
    {
        "title": _("Auth"),
        "separator": True,  # Top border
        "items": [
            {
                "title": _("Users"),
                "icon": "group",
                "link": reverse_lazy("admin:accounts_user_changelist"),
            },
        ],
    },
    {
        "title": _("Travel"),
        "separator": True,  # Top border
        "items": [
            {
                "title": _("Tour"),
                "icon": "tour",
                "link": reverse_lazy("admin:api_travelmodel_changelist"),
            },
            {
                "title": _("Order"),
                "icon": "shopping_cart",
                "link": reverse_lazy("admin:api_ordermodel_changelist"),
            },
            {
                "title": _("Contact"),
                "icon": "contacts",
                "link": reverse_lazy("admin:api_contactmodel_changelist"),
            },
        ],
    },
]
