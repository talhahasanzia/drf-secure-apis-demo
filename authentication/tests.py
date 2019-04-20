from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient, APIRequestFactory
from rest_framework.views import status

from authentication.views import UserView
from oauth_django.messages import *
from .serializers import UserResponseSerializer


# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_user(username="", password="", email=""):
        if username != "" and password != "" and email != "":
            User.objects.create_user(username, email, password)

    def setUp(self):
        # test users
        self.create_user("talha", "password123", "sample1@email.com")
        self.create_user("talha2", "password123", "sample2@email.com")
        self.create_user("talha3", "password123", "sample3@email.com")
        self.create_user("talha4", "password123", "sample4@email.com")


class GetUsersTest(BaseViewTest):

    def test_get_all_users(self):
        """
        This test ensures that all songs added in the setUp method
        exist when we make a GET request to the songs/ endpoint
        """
        serialized = UserResponseSerializer(User.objects.all(), many=True)
        expected = success(200, serialized.data)

        factory = APIRequestFactory()

        view = UserView.as_view()

        # Make an authenticated request to the view...
        request = factory.get('/users/')

        response = view(request)

        print(serialized.data)

        self.assertEqual(response.data, expected)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
