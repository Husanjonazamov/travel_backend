from rest_framework import serializers

from core.apps.api.models import TravelModel


class BaseTravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelModel
        fields = [
            "id",
            "name",
        ]


class ListTravelSerializer(BaseTravelSerializer):
    class Meta(BaseTravelSerializer.Meta): ...


class RetrieveTravelSerializer(BaseTravelSerializer):
    class Meta(BaseTravelSerializer.Meta): ...


class CreateTravelSerializer(BaseTravelSerializer):
    class Meta(BaseTravelSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
