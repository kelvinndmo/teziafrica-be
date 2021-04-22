from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions
from .models import *
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from rest_framework.decorators import action, permission_classes as permission_decorator
from rest_framework.permissions import AllowAny
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

# Create your views here.

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


def home(request):
    Profile = Profile.objects.all()
    business = Client.objects.all()
    
    return render(request, "home.html", {"profiles":profile, "client":client,"})


class ProfileViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing profile instances.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    
class ClientViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing client instances.
    """
    serializer_class = clientSerializer
    queryset = Client.objects.all()



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