from django.test import TestCase
from django.urls import reverse

class ShortenerViewTests(TestCase):
    def test_shortener_home_view(self):
        response = self.client.get(reverse('shortener_home'))

