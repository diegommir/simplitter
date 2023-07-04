from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Person

class PersonTestCase(APITestCase):
    """Test case for Person endpoints."""

    def setUp(self):
        """Set up method for this test case."""
        self.client = APIClient()
        self.url = '/person/'

    def test_add_person(self):
        """Test case to assert add a new Person."""
        data = {
            "username": "testuser",
            "name": "Test User"
        }

        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.count(), 1)
        self.assertEqual(Person.objects.get().username, data['username'])

    def test_add_person_missing_values(self):
        """Test case to assert input validation for adding Person."""

        #Missing username
        data = {
            "name": "Test User"
        }

        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Person.objects.count(), 0)

        #Missing name
        data = {
            "username": "testuser"
        }

        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Person.objects.count(), 0)

        #Empty values
        data = {
            "username": "",
            "name": ""
        }

        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Person.objects.count(), 0)
