from rest_framework_json_api import serializers, relations

from MPs.models import MP

class MPsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MP
        fields = (
            'url',
            'additional_name',
            'home_page',
            'family_name',
            'full_name',
            'gender',
            'given_name',
            'party',
            'twitter'
        )
