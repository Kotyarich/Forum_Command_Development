from django.contrib.postgres.fields import ArrayField
from django.db import models
from .utils import make_human_readable


class Map(models.Model):
    KEYWORD_MAX_LEN = 32
    # the first item is main
    todo = ArrayField(models.CharField(max_length=KEYWORD_MAX_LEN))
    doing = ArrayField(models.CharField(max_length=KEYWORD_MAX_LEN))
    review = ArrayField(models.CharField(max_length=KEYWORD_MAX_LEN))

    @property
    def todo_text(self):
        return '\n'.join(self.todo)

    @property
    def doing_text(self):
        return '\n'.join(self.doing)

    @property
    def review_text(self):
        return '\n'.join(self.review)

    def __str__(self):
        return make_human_readable(self, ['todo', 'doing', 'review'])
