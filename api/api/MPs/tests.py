from django.test import TestCase

from .models import Scraper


class MPsTest(TestCase):
    def test_gets_all_the_items_from_API(self):
        MPs = Scraper()
        self.assertIsNotNone(MPs.count)
        self.assertIsNotNone(MPs.num_pages)
        self.assertEqual(MPs.count, len(MPs.items))
