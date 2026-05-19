from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AccountFlowTests(TestCase):
    def test_signup_creates_and_logs_in_user(self):
        response = self.client.post(
            reverse("accounts:signup"),
            {
                "username": "newuser",
                "first_name": "New",
                "last_name": "User",
                "email": "newuser@example.com",
                "password1": "StrongPass123!",
                "password2": "StrongPass123!",
            },
        )

        self.assertRedirects(response, reverse("core:home"))
        self.assertTrue(User.objects.filter(username="newuser").exists())
        self.assertIn("_auth_user_id", self.client.session)

    def test_login_page_renders(self):
        response = self.client.get(reverse("accounts:login"))
        self.assertEqual(response.status_code, 200)
