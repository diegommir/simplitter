from django.db import models
from django_extensions.db.models import TimeStampedModel

class Person(TimeStampedModel):
    username = models.CharField(unique=True, max_length=30)
    name = models.CharField(max_length=100)

class PostType(models.TextChoices):
    NEW = 'N'
    COMMENT = 'C'
    REPOST = 'R'

class PostStatus(models.TextChoices):
    ACTIVE = 'A'
    DELETED = 'D'

class Post(TimeStampedModel):
    type = models.CharField(max_length=1, choices=PostType.choices)
    content = models.TextField(max_length=500)
    creator = models.ForeignKey(Person, on_delete=models.PROTECT)
    status = models.CharField(max_length=1, choices=PostStatus.choices, default=PostStatus.ACTIVE)
