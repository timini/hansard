from chat.models import Comment
from rest_framework import viewsets

from chat.serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comments to be viewed or edited.
    """
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    resource_name = 'comments'
