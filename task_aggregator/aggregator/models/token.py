from django.contrib.auth.models import User
from django.db import models
from .map import Map
from .service import Service


class Token(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    in_service_username = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
    map = models.OneToOneField(Map, on_delete=models.CASCADE)

    def __str__(self):
        token = self.token[:4] + '·' * (len(self.token) - 4)
        if self.service.type == Service.Type.GITHUB:
            return token

        domain = self.service.domain
        if self.service.type == Service.Type.GITLAB:
            return f'{domain} {token}'

        username = self.in_service_username
        return f'{domain} {username} {token}'


