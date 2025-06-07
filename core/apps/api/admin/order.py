from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import OrderModel


@admin.register(OrderModel)
class OrderAdmin(ModelAdmin):
    list_display = (
        "id",
        "name",
        "phone",
        "payment_type",
        "quantity",
        "status"
    )
