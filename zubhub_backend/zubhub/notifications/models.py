from django.utils import timezone
from django.db import models
from django.core.validators import FileExtensionValidator
import uuid 

from creators.models import Creator 

class Notification(models.Model):
    id = models.UUIDField()
    message = models.TextField(blank=False, null=True)
    recipient = models.ForeignKey(Creator, on_delete = models.CASCADE, null=True, related_name="notifications", blank=True)
    viewed = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)