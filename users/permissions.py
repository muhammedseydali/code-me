from rest_framework import permissions
from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_staff


class IsAdminOrOwner(BasePermission):
    """
    Custom permission to only allow admins or owners of an object to view/edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Allow admin users to view/edit any object
        if request.user.is_staff:
            return True

        # Allow authenticated non-admin users to view/edit their own user object
        return obj == request.user
    
    from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role.name == 'Admin'

class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.role.name == 'Manager'

class IsTeamLead(BasePermission):
    def has_permission(self, request, view):
        return request.user.role.name == 'Team Lead'

class IsTeamMember(BasePermission):
    def has_permission(self, request, view):
        return request.user.role.name == 'Team Member'

