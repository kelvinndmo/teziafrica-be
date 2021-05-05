from rest_framework.permissions import BasePermission


class IsTeziAdmin(BasePermission):
    """Grants client admins full access"""

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role ='TA'


class IsOwnerOrAdmin(BasePermission):
    """Grants client admins full access"""

    def has_object_permission(self, request, view, obj):
        user = request.user
        return user or request.user == obj.client_admin


class IsProfileOwner(BasePermission):
    """allow only profile owners to update profiles"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user