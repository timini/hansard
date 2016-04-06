from django.db import models

import uuid

from main.models import DateMixin


class Constituency(DateMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    constituency_type = models.CharField(max_length=1024)
    started_date = models.DateField()
    ended_date = models.DateField(blank=True)
    gss_code = models.CharField(max_length=512)
    os_name = models.CharField(max_length=512)
