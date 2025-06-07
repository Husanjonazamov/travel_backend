from django.contrib import admin
from unfold.admin import ModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin
from core.apps.api.models import TravelModel


@admin.register(TravelModel)
class TravelAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "price",
        "time",
        "status"
    )
