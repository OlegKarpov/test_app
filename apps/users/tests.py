import unittest

from django.contrib.auth import get_user_model
from django.test.client import Client
from django.urls import reverse


class LoginTestCase(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user('lennon@thebeatles.com', 'johnpassword')
        self.user.first_name = 'john'
        self.user.save()

    def test_login_required(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

    def test_login(self):
        self.client.login(username='lennon@thebeatles.com', password='johnpassword')
        response = self.client.get(reverse('user_page', kwargs={'slug': self.user.first_name}))
        self.assertEqual(response.status_code, 200)
