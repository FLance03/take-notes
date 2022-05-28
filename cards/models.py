from django.db import models

from .managers import *
from users.views import User


# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField(default='')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    checked = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(null=True, default=None)

    objects = models.Manager()
    unchecked_objects = UncheckedCardManager()
    checked_objects = CheckedCardManager()

    @classmethod
    def unchecked_user_cards(cls, user):
        return cls.unchecked_objects.filter(owner_id=user.id, date_deleted__isnull=True)


