import os
import django
from django.urls import path, include, reverse
from rest_framework import status

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mindnow.settings')
django.setup()

from django.contrib.auth.models import User
from rest_framework.test import APIClient, APITestCase, force_authenticate


class AuthTestCase(APITestCase):
    urlpatterns = [
        path('api/', include('rest_api.urls')),
    ]

    def setUp(self):
        user = User.objects.create(
            username="User",
            email="user@mail.com",
            first_name="Name",
            last_name="Last",
            is_superuser=False
        )
        user.set_password("Pw123456")
        user.save()

        user = User.objects.create(
            username="Admin",
            email="admin@mail.com",
            first_name="Admin",
            last_name="X",
            is_superuser=True
        )
        user.set_password("Pw123456")
        user.save()

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('rest_api:api_register')
        response = self.client.post(url,
                                    {
                                        "username": "ApiTest",
                                        "password": "Pw123456",
                                        "password2": "Pw123456",
                                        "email": "user@example.com",
                                        "first_name": "Api",
                                        "last_name": "Test"
                                    },
                                    format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        url = reverse('rest_api:auth_token')
        response = self.client.post(url, {"username": "User", "password": "Pw123456"}, format='json')
        self.assertEqual(response.status_code, 200)

    def test_get_location(self):
        user = User.objects.get(username='User')
        self.client.force_authenticate(user=user)
        response = self.client.get(reverse('rest_api:location-list'))
        self.assertEqual(response.status_code, 200)
