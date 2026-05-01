from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer



class MenuViewTest(TestCase):
    def setUp(self):
        # Initialize the test client
        self.client = APIClient()
        
        # Create temporary test data
        Menu.objects.create(item_title="IceCream", price=80, inventory=100)
        Menu.objects.create(item_title="Pizza", price=120, inventory=50)

    def test_getall(self):
        # Hit the API endpoint
        response = self.client.get('/restaurant/menu/')
        
        # Retrieve data from database and serialize it
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        
        # Check if the API response matches the serialized database data
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)