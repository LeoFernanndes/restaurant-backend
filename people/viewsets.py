from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from people.models import User
from people.serializers import UserSerializer


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
