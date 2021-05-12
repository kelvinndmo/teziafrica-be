from django.shortcuts import render
from rest_framework import generics, mixins, status, permissions
from rest_framework.response import Response
from authentication.models import User
from authentication.serializers import UserSerializer, RegisterationSerializer, LoginSerializer
from rest_framework.decorators import api_view
from utils.permissions import IsTeziAdmin, PostUserWritePermissions
from rest_framework.permissions import BasePermission, IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, SAFE_METHODS, IsAuthenticatedOrReadOnly

# Create your views here.

@api_view(['GET'])
def apiRequest(request):
    api_endpoints = {
        'Register': 'register/',
        'Login': 'login/',
        'Users List':'api/v1/allprofiles/view/',
        'User Detail View':'api/v1/profile/view/details/<int:pk>/',
        'User Create':'api/v1/profile/create/',
        'User Update':'api/v1/profile/update/<int:pk>/',
        'User Delete':'api/v1/profile/delete/<int:pk>/',
        'Articles Endpoints':'articles/',
        'FlowBuilder Endpoints':'flowbuilder/',
        'Ticket Endpoints':'tickets/'
    }
    return Response(api_endpoints)


class RegistrationAPIView(generics.CreateAPIView):
  serializer_class = RegisterationSerializer

  def post(self, request):
      serializer = self.serializer_class(data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()

      user_data = serializer.data

      response = {
          "user":dict(user_data),
          "message":"Account created successfully"
      }

      return Response(response, status=status.HTTP_201_CREATED)

class LoginAPIView(generics.CreateAPIView):
  serializer_class = LoginSerializer

  def post(self, request):
      serializer = self.serializer_class(data=request.data)
      serializer.is_valid(raise_exception=True)
    
      user_data = serializer.data

      response = {
          "user":dict(user_data),
          "message":"You have logged in successfully"
      }

      return Response(response, status=status.HTTP_201_CREATED)

class UserList(generics.ListAPIView):
  permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
  queryset = User.objects.all()
  serializer_class = UserSerializer
  # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserDetails(generics.RetrieveAPIView):
  permission_classes = [DjangoModelPermissionsOrAnonReadOnly, IsAuthenticatedOrReadOnly]
  queryset = User.objects.all()
  serializer_class = UserSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class UserCreate(generics.ListCreateAPIView, PostUserWritePermissions):
  permission_classes = [PostUserWritePermissions()]
  queryset = User.objects.all()
  serializer_class = UserSerializer
  # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
  permission_classes = (IsTeziAdmin,)


class UserUpdate(generics.RetrieveUpdateAPIView, PostUserWritePermissions):
  permission_classes = [PostUserWritePermissions()]
  queryset = User.objects.all()
  serializer_class = UserSerializer
  # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAdmin0rCompany]


class UserDelete(generics.RetrieveDestroyAPIView, PostUserWritePermissions):
  permission_classes = [PostUserWritePermissions()]
  queryset = User.objects.all()
  serializer_class = UserSerializer
  # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, IsAdmin0rCompany]