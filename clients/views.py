from django.shortcuts import render
from rest_framework import generics
from clients.models import client
from clients.serializers import ClientSerializer
from utils.permissions import IsTeziAdmin

# Create your views here.
class CreateListClientAPIView(generics.ListCreateAPIView)
    serializers_class = ClientSerializer
    queryset = Client.objects.all()
    Permission_classes = (IsTeziAdmin,)