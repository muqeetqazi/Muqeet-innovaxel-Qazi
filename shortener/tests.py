from django.test import TestCase
from django.urls import reverse
from .models import ShortURL

class ShortenerViewTests(TestCase):
    def setUp(self):
        self.url = "http://example.com"
        self.new_url = "http://newexample.com"
        self.short_code = "abc123"
        self.short_url = ShortURL.objects.create(url=self.url, short_code=self.short_code)

    def test_shortener_home_view(self):
        response = self.client.get(reverse('shortener_home'))
        self.assertEqual(response.status_code, 200)

    def test_create_short_url(self):
        response = self.client.post(reverse('shorten-url'), {'url': self.url}, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertTrue(ShortURL.objects.filter(url=self.url).exists())

    def test_retrieve_short_url(self):
        response = self.client.get(reverse('retrieve-url', args=[self.short_code]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('url'), self.url)

    def test_update_short_url(self):
        response = self.client.put(
            reverse('update-url', args=[self.short_code]), 
            {'url': self.new_url}, 
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.short_url.refresh_from_db()
        self.assertEqual(self.short_url.url, self.new_url)

    def test_delete_short_url(self):
        response = self.client.delete(reverse('delete-url', args=[self.short_code]))
        self.assertEqual(response.status_code, 204)
        self.assertFalse(ShortURL.objects.filter(short_code=self.short_code).exists())

    def test_url_stats(self):
        response = self.client.get(reverse('url-stats', args=[self.short_code]))
        self.assertEqual(response.status_code, 200)
        json_response = response.json()
        self.assertEqual(json_response.get('url'), self.url)
        self.assertEqual(json_response.get('access_count'), 0)  # Initially should be 0
