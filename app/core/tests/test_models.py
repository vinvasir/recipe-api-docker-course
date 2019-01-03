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

    def test_user_email_normalized(self):
        email = 'test@LONDONAPPDEV.COM'
        user = get_user_model().objects.create_user(
            email=email,
            password='feafaewfw'
        )

        self.assertEqual('test@londonappdev.com', user.email)

    def test_user_email_validation(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            'prat@pratter.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
