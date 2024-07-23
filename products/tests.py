from django.test import TestCase
from .models import Products

# Create your tests here.
class ProductTestCase(TestCase):
    def setUp(self):
        Products.objects.create(
            name = "감자",
            price = 1000.00,
            status = "판매중",
            quantity = 5
        )

    def test_product_exists(self):
        potato = Products.objects.get(name = "감자")

        self.assertEqual(potato.name, "감자")