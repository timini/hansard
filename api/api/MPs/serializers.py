from rest_framework_json_api import serializers, relations

from MPs.models import MP

class MPsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MP
        #fields = ('url', 'text', 'user', 'created_at', 'updated_at')
