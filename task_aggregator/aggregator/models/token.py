from django.contrib.auth.models import User
from django.db import models
from .map import Map
from .service import Service
from .utils import make_human_readable


class Token(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    in_service_username = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    map = models.OneToOneField(Map, on_delete=models.CASCADE)

    def __str__(self):
        return make_human_readable(self, ['user_id', 'service_id', 'in_service_username', 'token', 'map_id'])
