"""This module contains all the Model classes used in this app."""

from django.db import models
from django_extensions.db.models import TimeStampedModel

class Person(TimeStampedModel):
    """
    Class representing a Person that can interact within the app.

    Attributes
    ----------
    username : str
        a public unique name to identify the person
    name : str
        a name defined by the person
    status : str/enum
        a string identifier picked from a previous defined list/enum.
    """

    class Status(models.TextChoices):
        """
        Enum like class that defines the possible states of a Person.
        """
        ACTIVE = 'A'
        DELETED = 'D'
    
    username = models.CharField(unique=True, max_length=30)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=1, choices=Status.choices, default=Status.ACTIVE)

class Post(TimeStampedModel):
    """
    Class the represents a Post. Posts are the tools a Person uses to interact with other People.
    
    Attributes
    ----------
    type = str/enum
        a string identifier picked from a previous defined list/enum
    content = str
        the content of the Post
    creator = Person
        the Person who created this Post
    status = str/enum
        a string identifier picked from a previous defined list/enum.
    """

    class Status(models.TextChoices):
        """
        Enum like class that defines the possible states of a Post.
        """
        ACTIVE = 'A'
        DELETED = 'D'

    class Type(models.TextChoices):
        """
        Enum like class that defines the possible types of a Post.
        """
        NEW = 'N'
        COMMENT = 'C'
        REPOST = 'R'
    
    type = models.CharField(max_length=1, choices=Type.choices)
    content = models.TextField(max_length=500)
    creator = models.ForeignKey(Person, on_delete=models.PROTECT)
    status = models.CharField(max_length=1, choices=Status.choices, default=Status.ACTIVE)
