from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
#
class AdvertisementStatusChoices(models.TextChoices):
    """Статусы объявления."""
    OPEN = "OPEN", "Открыто"
    CLOSED = "CLOSED", "Закрыто"
#
class Advertisement(models.Model):
    """Объявление."""
    title = models.CharField(max_length=100)
    description = models.TextField(default='')
    status = models.TextField(choices=AdvertisementStatusChoices.choices, default=AdvertisementStatusChoices.OPEN)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)