from django.test import TestCase
from django.urls import resolve, reverse
from shopp.views import home


class TestURL(TestCase):
    def test_home(self):
        url = reverse('product_by_category', args=['demo-slug'])
        self.assertEqual(resolve(url).func, home)
