from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.apps.api.views import TravelView

router = DefaultRouter()
router.register(r"travel", TravelView, basename="travel")


urlpatterns = [
    path("", include(router.urls)),
]
