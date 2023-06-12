from django.test import TestCase
from rest_framework.test import APIClient
from Restaurant.models import Menu
from Restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test instances of Menu model
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=120, inventory=50)
        Menu.objects.create(title="Burger", price=60, inventory=80)

    def test_getall(self):
        # Initialize APIClient
        client = APIClient()

        # Send GET request to the menu endpoint
        response = client.get('/menu/')

        # Retrieve all Menu objects and serialize them
        menu_items = Menu.objects.all()
        serializer = MenuSerializer(menu_items, many=True)

        # Assert that the serialized data equals the response data
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)
