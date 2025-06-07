from rest_framework import serializers

from core.apps.api.models import OrderModel


class BaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = [
            "id",
            "name",
            "phone",
            "payment_type",
            "quantity",
            "description",
            "status"
            
        ]


class ListOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta): ...


class RetrieveOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta): ...


class CreateOrderSerializer(BaseOrderSerializer):
    class Meta(BaseOrderSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
