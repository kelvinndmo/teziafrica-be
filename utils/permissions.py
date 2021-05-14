# from rest_framework import permissions
from rest_framework.permissions import BasePermission
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwner(BasePermission):
    """ a user can be able to edit an item enquiry belonging to them """
    
    message = 'Restricted to owner only!'

    def has_object_permission(self, request, view, obj):

        user = request.user

        if request.method in SAFE_METHODS:
            return True

        return obj.id == user.id



class IsAdminOrReadOnly(BasePermission):
    """ Check if user is admin and logged in then grants access."""

    message = 'Restricted to admin only!'

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            request.user.role == 'AD'
        )


class IsCompanyAdmin(BasePermission):
    """Grants approved Company admins full access"""

    message = 'Restricted to approved company only!'

    def has_permission(self, request, view):
        user = request.user if request.user.is_authenticated else None
        if user:
            company = user.employer.first()
            return company and user.role == 'CO' and \
                company.approval_status == 'approved'


class IsStaffOrReadOnly(BasePermission):
    """ Check if user is staff and logged in then grants access."""
    
    message = 'Restricted to staff only!'

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            request.user.role == 'ST'
        )


class IsClientOrReadOnly(BasePermission):
    """ Check if user is client logged in then grants access."""
    
    message = 'Restricted to client only!'

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            request.user.role == 'CL'
        )