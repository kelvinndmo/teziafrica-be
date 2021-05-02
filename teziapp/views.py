from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions
from .models import *
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from rest_framework.decorators import action, permission_classes as permission_decorator
from rest_framework.permissions import AllowAny
from django.contrib.auth import login

# Create your views here.
class IsAssigned(permissions.BasePermission): 
    """
    Only person who assigned has permission
    """
    def has_object_permission(self, request, view, obj):
		# check if user who launched request is object owner 
        if obj.assigned_to == request.user: 
            return True
        return False
class IsReadOnlyOrIsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        authenticated = request.user.is_authenticated
        if not authenticated:
            if view.action == '/':
                return True
            else:
                return False
        else:
            return True