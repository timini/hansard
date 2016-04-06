from django.contrib import admin

from .models import MP


class MPAdmin(admin.ModelAdmin):
    list_display = (
        'source_id',
        'additional_name',
        'home_page',
        'family_name',
        'full_name',
        'gender',
        'given_name',
        'party',
        'twitter',
    )

admin.site.register(MP, MPAdmin)
