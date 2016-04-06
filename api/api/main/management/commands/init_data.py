from django.core.management.base import BaseCommand, CommandError

from pprint import pprint

from MPs.models import MP
from constituencies.models import Constituency
from main.models import Scraper


class Command(BaseCommand):
    help = 'Retrevies MP data from the parlimentary website and loads into the database'

    def handle(self, *args, **options):
        print('fetching member data from data.gov.uk')
        members = Scraper(dataset='members')
        print('fetching constituency data from data.gov.uk')
        constituencies = Scraper(dataset='constituencies', label_key='name')

        print('commiting members to db')
        MP.objects.all().delete()
        MP.objects.bulk_create([
            MP(**item) for item in members.cleaned_items
        ])

        print('commiting constituencies to db')
        Constituency.objects.all().delete()
        Constituency.objects.bulk_create([
            Constituency(**item) for item in constituencies.cleaned_items
        ])

        print('updating members with links to constituencies')

        def get_mp_id_from_item(item):
            _id = int(item['_about'].split('/')[-1])
            return MP.objects.get(source_id=_id).id

        def get_constituency_id_from_item(item):
            _id = int(item['constituency']['_about'].split('/')[-1])
            return Constituency.objects.get(source_id=_id).id

        Through = MP.constituency.through
        Through.objects.all().delete()
        Through.objects.bulk_create([
            Through(
                mp_id = get_mp_id_from_item(item),
                constituency_id = get_constituency_id_from_item(item)
            )
            for item in members.items
            if 'constituency' in item.keys()
        ])
        print('complete')
