from django.contrib.auth import get_user_model
from django.test import TestCase


class ModelTest(TestCase):
    def test_create_a_user_with_email_successfully(self):
        """Test creating a new user with an email is successful"""
        email = 'test@example.com'
        password = 'password123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(email, user.email)
        self.assertTrue(user.check_password(password))