from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import TravelModel


@receiver(post_save, sender=TravelModel)
def TravelSignal(sender, instance, created, **kwargs): ...
