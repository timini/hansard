from rest_framework import viewsets

from .serializers import ConstituenciesSerializer
from .models import Constituency


class ConstituenciesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Constituencies to be viewed or edited.
    """
    queryset = Constituency.objects.all()#.order_by('-created_at')
    serializer_class = ConstituenciesSerializer
    resource_name = 'constituencies'
