from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel




class TypeTour(models.TextChoices):
    tour = "tour", _("Tour")
    hotel = "hotel", _("Hotel")
    transfer = "transfer", _("Transfer")

class StatusChoice(models.TextChoices):
    open = "open", _("Ochiq")
    close = "close", _("Yopiq")


class TravelModel(AbstractBaseModel):
    name = models.CharField(
        verbose_name=_("Nomi"),
        max_length=255,
        blank=True, null=True
    )
    description = models.TextField(
        verbose_name=_("Tavsif"),
        blank=True, null=True
    )
    location = models.CharField(
        verbose_name=_("Manzil"),
        max_length=100,
        blank=True, null=True
    )
    time = models.CharField(
        verbose_name=_("Vaqt"),
        max_length=150,
        blank=True, null=True
    )
    image = models.ImageField(
        verbose_name=_("Rasm"),
        upload_to="travel_image/",
        blank=True, null=True
    )
    price = models.CharField(
        verbose_name=_("Narx"),
        max_length=150,
        blank=True, null=True
    )
    type = models.CharField(
        verbose_name=_("Turi"),
        max_length=150,
        blank=True, null=True,
        choices=TypeTour.choices,
        default=TypeTour.tour
    )
    status = models.CharField(
        verbose_name=_("Status"),
        max_length=100,
        blank=True, null=True,
        choices=StatusChoice.choices,
        default=StatusChoice.open
        
    )
    

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "travel"
        verbose_name = _("TravelModel")
        verbose_name_plural = _("TravelModels")
