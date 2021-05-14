from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from authentication.models import User, Company, Staff
from authentication.serializers import UserSerializer, RegisterationSerializer, LoginSerializer, CompanySerializer, StaffSerializer
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAdminUser
from utils.permissions import IsOwner, IsAdminOrReadOnly, IsStaffOrReadOnly, IsCompanyAdmin

# Create your views here.

@api_view(['GET'])
def apiRequest(request):
    api_endpoints = {
        # 'Swagger Endpoints View': '/swagger/',
        'API Documentation': '/redoc/',
        'Register': '/register/',
        'Login': '/login/',
        'Users List':'api/v1/allprofiles/view/',
        'User Detail View':'api/v1/profile/view/details/<int:pk>/',
        'User Create':'api/v1/profile/create/',
        'User Update':'api/v1/profile/update/<int:pk>/',
        'User Delete':'api/v1/profile/delete/<int:pk>/',

        'Companies List':'api/v1/allcompanies/view/',
        'Company Detail View':'api/v1/company/view/details/<int:pk>/',
        'Company Create':'api/v1/company/create/',
        'Company Update':'api/v1/company/update/<int:pk>/',
        'Company Delete':'api/v1/company/delete/<int:pk>/',

        'Staff List':'api/v1/allstaff/view/',
        'Staff Detail View':'api/v1/staff/view/details/<int:pk>/',
        'Staff Create':'api/v1/staff/create/',
        'Staff Update':'api/v1/staff/update/<int:pk>/',
        'Staff Delete':'api/v1/staff/delete/<int:pk>/',

        'Articles Endpoints':'articles/',
        'FlowBuilder Endpoints':'flowbuilder/',
        'Ticket Endpoints':'tickets/'
    }
    return Response(api_endpoints)


class RegistrationAPIView(generics.CreateAPIView):
  serializer_class = RegisterationSerializer
  permission_classes = [permissions.AllowAny]

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
  permission_classes = [permissions.AllowAny]

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
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [IsAdminUser]


class UserDetails(generics.RetrieveAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [IsAdminUser]


class UserCreate(generics.ListCreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [IsAdminOrReadOnly]


class UserUpdate(generics.RetrieveUpdateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [IsOwner]
  

class UserDelete(generics.RetrieveDestroyAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [IsAdminOrReadOnly] 



class CompanyList(generics.ListAPIView):
  queryset = Company.objects.all()
  serializer_class = CompanySerializer
  permission_classes = [IsAdminUser]


class CompanyDetails(generics.RetrieveAPIView):
  queryset = Company.objects.all()
  serializer_class = CompanySerializer
  permission_classes = [IsCompanyAdmin] 
  
class CompanyCreate(generics.ListCreateAPIView):
  queryset = Company.objects.all()
  serializer_class = CompanySerializer
  permission_classes = [IsAdminOrReadOnly]


class CompanyUpdate(generics.RetrieveUpdateAPIView):
  queryset = Company.objects.all()
  serializer_class = CompanySerializer
  permission_classes = [IsOwner]

class CompanyDelete(generics.RetrieveDestroyAPIView):
  queryset = Company.objects.all()
  serializer_class = CompanySerializer
  permission_classes = [IsAdminOrReadOnly]



class StaffList(generics.ListAPIView):
  queryset = Staff.objects.all()
  serializer_class = StaffSerializer
  permission_classes = [IsAdminUser]


class StaffDetails(generics.RetrieveAPIView):
  queryset = Staff.objects.all()
  serializer_class = StaffSerializer
  permission_classes = [IsStaffOrReadOnly]
  
  
class StaffCreate(generics.ListCreateAPIView):
  queryset = Staff.objects.all()
  serializer_class = StaffSerializer
  permission_classes = [IsCompanyAdmin]


class StaffUpdate(generics.RetrieveUpdateAPIView):
  queryset = Staff.objects.all()
  serializer_class = StaffSerializer
  permission_classes = [IsOwner]

class StaffDelete(generics.RetrieveDestroyAPIView):
  queryset = Staff.objects.all()
  serializer_class = StaffSerializer
  permission_classes = [IsOwner]