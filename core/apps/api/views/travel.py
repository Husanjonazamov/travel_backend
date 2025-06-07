from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.api.models import TravelModel
from core.apps.api.serializers.travel import CreateTravelSerializer, ListTravelSerializer, RetrieveTravelSerializer


@extend_schema(tags=["travel"])
class TravelView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = TravelModel.objects.all()
    serializer_class = ListTravelSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListTravelSerializer,
        "retrieve": RetrieveTravelSerializer,
        "create": CreateTravelSerializer,
    }
