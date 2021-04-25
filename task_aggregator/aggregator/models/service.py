from django.db import models


class Service(models.Model):
    class Type(models.IntegerChoices):
        GITHUB = 1
        GITLAB = 2
        JIRA = 3

    # with schema, e. g. https://api.github.com
    domain = models.CharField(max_length=255)

    type = models.IntegerField(choices=Type.choices)

    def __str__(self):
        if self.type == self.Type.GITHUB:
            return 'GitHub'
        if self.type == self.Type.GITLAB:
            return 'GitLab'
        return 'Jira'
