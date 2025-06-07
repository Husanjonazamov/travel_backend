from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import ContactModel


@admin.register(ContactModel)
class ContactAdmin(ModelAdmin):
    list_display = (
        "id",
        "name",
        "email",
        "phone"
    )
