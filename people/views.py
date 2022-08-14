from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from people.models import User
from people.serializers import CustomTokenObtainPairSerializer, UpdateUserRoleSerializer
from people.permissions import UpdateUserRolePermission


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UpdateUserRoleApiView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserRoleSerializer
    permission_classes = [IsAuthenticated, UpdateUserRolePermission]


