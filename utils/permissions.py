# from rest_framework import permissions
from rest_framework.permissions import BasePermission
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwner(BasePermission):
    """ a user can be able to edit a property enquiry belonging to only him """
    
    message = 'Editting restricted to owner only!'

    def has_object_permission(self, request, view, obj):

        user = request.user

        if request.method in SAFE_METHODS:
            return True

        return obj.requester == user

class IsAdminOrReadOnly(BasePermission):
    """ Check if user is admin and logged in then grants access."""

    message = 'Editting restricted to admin only!'

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            request.user.role == 'AD'
        )

class IsCompanyOrReadOnly(BasePermission):
    """ Check if user is admin and logged in then grants access."""
    
    message = 'Editting restricted to company only!'

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            request.user.role == 'CO'
        )


class IsStaffOrReadOnly(BasePermission):
    """ Check if user is admin and logged in then grants access."""
    
    message = 'Editting restricted to staff only!'

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            request.user.role == 'ST'
        )


class IsClientOrReadOnly(BasePermission):
    """ Check if user is admin and logged in then grants access."""
    
    message = 'Editting restricted to client only!'

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            request.user.role == 'CL'
        )





