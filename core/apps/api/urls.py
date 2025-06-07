from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.apps.api.views import (
    TravelView, OrderView, ContactView
)

router = DefaultRouter()
router.register(r"travel", TravelView, basename="travel")
router.register(r"order", OrderView, basename="order")
router.register(r"contact", ContactView, basename="contact")

urlpatterns = [
    path("", include(router.urls)),
]
