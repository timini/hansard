from rest_framework_json_api import serializers, relations

from .models import Constituency

class ConstituenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Constituency
        fields = (
            'url',
            'name',
            'constituency_type',
            'started_date',
            'ended_date',
            'gss_code',
            'os_name',
        )
