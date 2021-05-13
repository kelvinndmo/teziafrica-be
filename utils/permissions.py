# from rest_framework import permissions
from rest_framework.permissions import BasePermission
from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwner(BasePermission):
    """ a user can be able to edit an item enquiry belonging they own """
    
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
    """ Check if user is company and logged in then grants access."""
    
    message = 'Editting restricted to company only!'

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            request.user.role == 'CO'
        )



class IsStaffOrReadOnly(BasePermission):
    """ Check if user is staff and logged in then grants access."""
    
    message = 'Editting restricted to staff only!'

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            request.user.role == 'ST'
        )


class IsClientOrReadOnly(BasePermission):
    """ Check if user is client logged in then grants access."""
    
    message = 'Editting restricted to client only!'

    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated and
            request.user.role == 'CL'
        )


class IsCompanyAdmin(BasePermission):
    """Grants approved Company admins full access"""

    def has_permission(self, request, view):
        user = request.user if request.user.is_authenticated else None
        if user:
            company = user.employer.first()
            return company and user.role == 'CA' and \
                company.approval_status == 'approved'


class CanEditItem(BasePermission):
    """Company admins should be able to edit items they own"""

    def has_object_permission(self, request, view, obj):

        user = request.user
        if request.method in SAFE_METHODS:
            return True
        if user.is_authenticated and user.role == 'C0':
            return user == obj.company.company_admin
        if user.is_authenticated and user.role == 'AD':
            return True
        return False