from django.http import HttpResponse
from django.urls import resolve
from django.test import TestCase
from lists.views import home_page

class HomePageTest(TestCase):
    def test_use_home_page(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
        