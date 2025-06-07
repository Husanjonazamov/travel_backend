from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class ContactModel(AbstractBaseModel):
    name = models.CharField(
        verbose_name=_("Ism && Familya"),
        max_length=255, 
        blank=True, null=True
    )
    email = models.EmailField(
        verbose_name=_("Email"),
        blank=True, null=True
    )
    phone = models.CharField(
        verbose_name=_("Telefon")
    )
    description = models.TextField(
        verbose_name=_("Xabar"),
        blank=True, null=True
    )

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "contact"
        verbose_name = _("ContactModel")
        verbose_name_plural = _("ContactModels")
