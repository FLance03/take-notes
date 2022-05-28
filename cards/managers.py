from django.db import models


class UncheckedCardManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(checked=False)


class CheckedCardManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(checked=True)