from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class ContactModel(AbstractBaseModel):

    name = models.CharField(verbose_name=_("name"), max_length=255)

    def __str__(self):
        return self.pk

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "contact"
        verbose_name = _("ContactModel")
        verbose_name_plural = _("ContactModels")
