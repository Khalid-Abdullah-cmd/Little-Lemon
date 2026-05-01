from django.test import TestCase
from restaurant.models import Menu


class MenuTest(TestCase):
    def test_get_item(self):
        # Create a temporary item in the test database
        item = Menu.objects.create(item_title="IceCream", price=80, inventory=100)
        
        # Test if the string representation matches what we expect
        self.assertEqual(str(item), "IceCream : 80")