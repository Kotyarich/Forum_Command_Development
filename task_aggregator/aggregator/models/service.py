from django.db import models
from .utils import make_human_readable


class Service(models.Model):
    class Type(models.IntegerChoices):
        GITHUB = 1
        GITLAB = 2
        JIRA = 3

    # with schema, e. g. https://api.github.com
    domain = models.CharField(max_length=255)

    type = models.IntegerField(choices=Type.choices)

    def __str__(self):
        return make_human_readable(self, ['domain', 'type'])
