from django.core.management.base import BaseCommand, CommandError

from MPs.models import MP
from constituencies.models import Constituency
from main.models import Scraper


class Command(BaseCommand):
    help = 'Retrevies MP data from the parlimentary website and loads into the database'

    def handle(self, *args, **options):
        members = Scraper(dataset='members')
        constituencies = Scraper(dataset='constituencies', label_key='name')

        MP.objects.all().delete()
        MP.objects.bulk_create([
            MP(**item) for item in members.cleaned_items
        ])

        Constituency.objects.all().delete()
        Constituency.objects.bulk_create([
            Constituency(**item) for item in constituencies.cleaned_items
        ])
