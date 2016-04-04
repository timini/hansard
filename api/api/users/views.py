from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer

# Method the current user can use to find their user ID
@api_view(['GET'])
def current_user(request):
    if request.user.is_authenticated():
        return Response({'id': request.user.id,})
    return Resonse({})

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    resource_name = 'users'
