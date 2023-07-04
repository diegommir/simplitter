"""This module contains all the API endpoints used in this app."""

from django.db.models import Q
from rest_framework import views, status
from rest_framework.response import Response
from .serializers import PersonSerializer
from .models import Person
from rest_framework.viewsets import ModelViewSet

class PersonAPI(views.APIView):
    """
    Handles all requests to the Person API.
    
    Methods
    -------
    get
        Return a list of all Person class in database
    post
        Save a new Person to the database
    """

    def get(self, request):
        """Return a list of all Person class in database."""
        persons = Person.objects.all()

        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """Save a new Person to the database."""
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonIdAPI(views.APIView):
    """
    Handles all requests for the Person with the given id.
    
    Methods
    -------
    get(id)
        Return one Person from database based on the given id
    delete(id)
        Delete one Person from the database based on the given id
    """

    def get(self, request, id):
        """Return one Person from database based on the given id."""
        try:
            person = Person.objects.get(Q(id=id) & Q(status=Person.Status.ACTIVE))

            serializer = PersonSerializer(person)
            return Response(serializer.data)
        except Person.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def patch(self, request, id):
        """Update a Person given the id."""
        try:
            person = Person.objects.get(Q(id=id) & Q(status=Person.Status.ACTIVE))

            serializer = PersonSerializer(instance=person, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Person.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    
    def delete(self, request, id):
        """Change status of a Person to DELETED based on the given id."""
        try:
            person = Person.objects.get(Q(id=id) & Q(status=Person.Status.ACTIVE))

            return Response({"message":f"Person {person.username} updated successfully."})
        except Person.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
