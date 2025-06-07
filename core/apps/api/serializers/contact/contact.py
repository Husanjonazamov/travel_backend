from rest_framework import serializers

from core.apps.api.models import ContactModel


class BaseContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = [
            "id",
            "name",
            "email",
            "phone",
            "description"
        ]


class ListContactSerializer(BaseContactSerializer):
    class Meta(BaseContactSerializer.Meta): ...


class RetrieveContactSerializer(BaseContactSerializer):
    class Meta(BaseContactSerializer.Meta): ...


class CreateContactSerializer(BaseContactSerializer):
    class Meta(BaseContactSerializer.Meta):
        fields = [
            "id",
            "name",
            "email",
            "phone",
            "description"
        ]
