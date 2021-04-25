from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='user',
                                on_delete=models.CASCADE)
    deadline_range = models.IntegerField(default=24)
    notifications_enabled = models.BooleanField(default=False)
    notifications_sound = models.BooleanField(default=False)
