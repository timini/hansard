from django.db import models

import uuid

from main.models import DateMixin


class Constituency(DateMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=1024)
    source_id = models.IntegerField(unique=True, blank=True)
    constituency_type = models.CharField(max_length=1024)
    started_date = models.DateField()
    ended_date = models.DateField(blank=True, null=True)
    gss_code = models.CharField(max_length=512)
    os_name = models.CharField(max_length=512)
