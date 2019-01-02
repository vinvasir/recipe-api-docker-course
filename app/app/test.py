from django.test import TestCase

from app.calc import add, subtract


class CalcTest(TestCase):
    def test_add_numbers(self):
        """
        Test that two numbers are added together
        :return: int
        """
        x = 5
        y = 4
        self.assertEqual(9, add(x, y))

    def test_substract_numbers(self):
        """Test that values are subtracted and returned"""
        self.assertEqual(6, subtract(5, 11))
