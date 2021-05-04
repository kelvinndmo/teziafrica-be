from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .serializers import CompanySerializer
from .models import Company
from rest_framework.views import APIView
from django.contrib.auth.models import User


# Company APIView

class ListCompanyAPIView(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CreateCompanyAPIView(CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
class UpdateCompanyAPIView(UpdateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
class DeleteCompanyAPIView(DestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer   





