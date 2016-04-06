from MPs.models import MP
from rest_framework import viewsets

from MPs.serializers import MPsSerializer


class MPsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows MPs to be viewed or edited.
    """
    queryset = MP.objects.all()#.order_by('-created_at')
    serializer_class = MPsSerializer
    resource_name = 'member_of_parliment'
