from django.core.management.base import BaseCommand, CommandError
from MPs.models import MP, Scraper, camel_to_snake

class Command(BaseCommand):
    help = 'Retrevies MP data from the parlimentary website and loads into the database'

    def handle(self, *args, **options):
        scraped = Scraper(dataset='members', excluded_keys=['constituency'])
        MP.objects.all().delete()
        MP.objects.bulk_create([
            MP(**item) for item in scraped.cleaned_items
        ])
