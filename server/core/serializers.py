"""This module contains all the Serializer classes used in this app."""

from rest_framework.serializers import ModelSerializer
from . import models

class PersonSerializer(ModelSerializer):
    """Serializer class for the Person model."""
    class Meta:
        model = models.Person
        fields = ['id', 'username', 'name', 'status', 'created', 'modified']

class PostSerializer(ModelSerializer):
    """Serializer class for the Post model."""
    class Meta:
        model = models.Post
        fields = ['id', 'type', 'content', 'creator', 'status', 'created', 'modified']
