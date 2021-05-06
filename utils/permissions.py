# from rest_framework import permissions
from rest_framework.permissions import BasePermission
from rest_framework.permissions import BasePermission, IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, SAFE_METHODS

class PostUserWritePermissions(BasePermission):
  message = 'only the auther can edit this!'
  def has_object_permission(self, request, view, obj):
    if request.method in SAFE_METHODS:
      return True
    return obj.author == request.user

class IsTeziAdmin(BasePermission):
    def has_object_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'CL'
