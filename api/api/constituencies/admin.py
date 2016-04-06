from django.contrib import admin

from .models import Constituency


class ConstituenciesAdmin(admin.ModelAdmin):
    list_display = (
        'source_id',
        'name',
        'constituency_type',
        'started_date',
        'ended_date',
        'gss_code',
        'os_name',
    )

admin.site.register(Constituency, ConstituenciesAdmin)
