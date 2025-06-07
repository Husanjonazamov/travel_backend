from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import TravelModel


@admin.register(TravelModel)
class TravelAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
