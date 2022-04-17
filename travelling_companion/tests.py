from decorator_include import decorator_include
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase, override_settings
from django.urls import reverse, path

from travelling_companion.views import TripListView


class BaseAuthTest(TestCase):
    urlpatterns = [
        path('', decorator_include(login_required, 'travelling_companion.urls')),
    ]

    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='user', email='user@mail.com', password='top_secret')

    def test_home(self):
        request = self.factory.get(reverse('travelling_companion:home'))
        request.user = self.user
        response = TripListView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_home_auth(self):
        request = self.factory.get(reverse('travelling_companion:home'))
        request.user = AnonymousUser()
        response = TripListView.as_view()(request)
        self.assertEqual(response.status_code, 302)


class LoginTestCase(TestCase):
    urlpatterns = [
        path('', decorator_include(login_required, 'travelling_companion.urls')),
    ]

    def test_login(self):
        response = self.client.get('/')
        self.assertRedirects(response, '/auth/login/?next=/')
