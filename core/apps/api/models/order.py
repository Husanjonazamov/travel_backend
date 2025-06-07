from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel



class PaymentType(models.TextChoices):
    click = "click", _("Click")
    payme = "payme", _("Payme")
    vise = "vise", _("Visa")




class OrderModel(AbstractBaseModel):
    name = models.CharField(
        verbose_name=_("Ism"),
        max_length=255,
    )
    phone = models.CharField(
        verbose_name=_("Telefon"),
        max_length=150,
        blank=True, null=True
    )
    payment_type = models.CharField(
        verbose_name=_("To'lov turi"),
        max_length=100,
        choices=PaymentType.choices,
        default=PaymentType.payme
    )
    quantity = models.IntegerField(
        verbose_name=_("Chipta Soni"),
        max_length=100,
        blank=True, null=True
    )
    description = models.TextField(
        verbose_name=_("Tavsif"),
        blank=True, null=True
    )
    status = models.BooleanField(
        verbose_name=_("Status"),
        default=True
    )

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "order"
        verbose_name = _("OrderModel")
        verbose_name_plural = _("OrderModels")
