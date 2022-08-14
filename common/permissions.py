from rest_framework.permissions import BasePermission

from common.models import PersonAddress
from people.models import User


class PersonAddressCrudPermission(BasePermission):
    def has_permission(self, request, view):
        user_pk = view.kwargs['user_pk']
        if request.user == User.objects.get(id=user_pk):
            return True
        return False
