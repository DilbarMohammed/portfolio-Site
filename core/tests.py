from django.test import TestCase
from django.urls import reverse


class PageSmokeTests(TestCase):
    def test_public_pages_render(self):
        for url_name in ["core:home", "core:about", "core:projects", "contacts:contact"]:
            response = self.client.get(reverse(url_name))
            self.assertEqual(response.status_code, 200)
