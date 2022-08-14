from rest_framework.permissions import BasePermission


class UpdateUserRolePermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'admin':
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user != obj:
            return True
        return False