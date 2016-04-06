from django.test import TestCase

from main.models import Scraper

from .models import Constituency

class ConstituenciesTest(TestCase):
    def setUp(self):
        self.scraper = Scraper(dataset='constituencies', label_key='name')

    def test_gets_all_the_items_from_API(self):
        self.assertIsNotNone(self.scraper.count)
        self.assertIsNotNone(self.scraper.num_pages)
        self.assertEqual(self.scraper.count, len(self.scraper.items))
        self.assertEqual(self.scraper.count, len(self.scraper.cleaned_items))

    def test_create_object_from_Scraper(self):
        obj = Constituency(**self.scraper.cleaned_items[0])
        obj.save()
        self.assertIsInstance(obj, Constituency)
        # test for the source_id value
        _id = int(self.scraper.items[0]['_about'].split('/')[-1])
        name = self.scraper.items[0]['label']['_value']
        self.assertEqual(obj.source_id, _id)
        self.assertEqual(obj.name, name)
