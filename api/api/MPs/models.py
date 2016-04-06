from django.db import models

import uuid
from pprint import pprint

from main.models import DateMixin, Scraper


class MP(DateMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    additional_name = models.CharField(max_length=1024, blank=True)
    home_page = models.URLField(blank=True)
    #constituency = models.ManyToManyField(Constituency, blank=True)
    family_name = models.CharField(max_length=1024)
    full_name = models.CharField(max_length=1024)
    gender = models.CharField(
        max_length=2,
        choices=(
            ('M','Male'),
            ('F','Female')
        )
    )
    given_name = models.CharField(max_length=1024, blank=True)
    party = models.CharField(max_length=512, blank=True)
    twitter = models.URLField(blank=True)
