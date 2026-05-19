from django.test import TestCase
from django.urls import reverse

from .models import ContactSubmission


class ContactSubmissionTests(TestCase):
    def test_contact_form_creates_submission(self):
        response = self.client.post(
            reverse("contacts:contact"),
            {
                "name": "Jordan Lee",
                "email": "jordan@example.com",
                "phone": "",
                "subject": "Portfolio inquiry",
                "message": "I would like to discuss a Django project.",
            },
        )

        self.assertRedirects(response, reverse("contacts:contact"))
        self.assertEqual(ContactSubmission.objects.count(), 1)
