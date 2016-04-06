from rest_framework_json_api import serializers, relations

from MPs.models import MP
from constituencies.models import Constituency

class MPsSerializer(serializers.ModelSerializer):
    constituency = relations.ResourceRelatedField(
        queryset=Constituency.objects.all(),
        pk_field=serializers.UUIDField(format='hex_verbose'),
        many=True,
        read_only=False
    )
    class Meta:
        model = MP
        fields = (
            'url',
            'constituency',
            'additional_name',
            'home_page',
            'family_name',
            'full_name',
            'gender',
            'given_name',
            'party',
            'twitter'
        )
