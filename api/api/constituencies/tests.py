from django.test import TestCase

from main.models import Scraper

from .models import Constituency

class ConstituenciesTest(TestCase):
    def setUp(self):
        self.scraper = Scraper(dataset='constituencies')

    def test_gets_all_the_items_from_API(self):
        self.assertIsNotNone(self.scraper.count)
        self.assertIsNotNone(self.scraper.num_pages)
        self.assertEqual(self.scraper.count, len(self.scraper.items))
        self.assertEqual(self.scraper.count, len(self.scraper.cleaned_items))

    def test_create_object_from_Scraper(self):
        obj = Constituency(**self.scraper.cleaned_items[0])
        obj.save()
        self.assertIsInstance(obj, Constituency)
