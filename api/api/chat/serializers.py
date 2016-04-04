from rest_framework_json_api import serializers, relations

from chat.models import Comment
from users.models import User


class CommentSerializer(serializers.ModelSerializer):
    user = relations.ResourceRelatedField(
        queryset=User.objects.all(),
        pk_field=serializers.UUIDField(format='hex_verbose'),
        many=False,
        read_only=False
    )
    class Meta:
        model = Comment
        fields = ('url', 'text', 'user', 'created_at', 'updated_at')
