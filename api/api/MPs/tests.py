from django.test import TestCase

from main.models import Scraper

from .models import MP

class MPsTest(TestCase):
    def setUp(self):
        self.scraper = Scraper(dataset='members', excluded_keys=['constituency'])

    def test_scraper_without_excluding_related_relationship_key(self):
        s = Scraper(dataset='members')

    def test_gets_all_the_items_from_API(self):
        self.assertIsNotNone(self.scraper.count)
        self.assertIsNotNone(self.scraper.num_pages)
        self.assertEqual(self.scraper.count, len(self.scraper.items))
        self.assertEqual(self.scraper.count, len(self.scraper.cleaned_items))
        self.assertNotIn('constituency', self.scraper.cleaned_items[0].keys())
        self.assertNotIn('constituency', self.scraper.cleaned_items[-1].keys())

    def test_create_object_from_scrapers_cleaned_items(self):
        obj = MP(**self.scraper.cleaned_items[0])
        obj.save()
        self.assertIsInstance(obj, MP)
