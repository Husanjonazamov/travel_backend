from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import TravelModel


@register(TravelModel)
class TravelTranslation(TranslationOptions):
    fields = []
