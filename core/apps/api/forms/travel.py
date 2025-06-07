from django import forms

from core.apps.api.models import TravelModel


class TravelForm(forms.ModelForm):

    class Meta:
        model = TravelModel
        fields = "__all__"
