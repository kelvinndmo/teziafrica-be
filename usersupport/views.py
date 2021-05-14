from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from usersupport.models import SupportRequest, SupportFeedback
from .serializers import SupportRequestSerializer, SupportFeedbackSerializer
from rest_framework.decorators import api_view
from utils.permissions import IsOwner, IsAdminOrReadOnly

# Create your views here.

@api_view(['GET'])
def apiRequest(request):
    api_endpoints = {
        'Support Requests List':'support/api/v1/allsupportrequests/view',
        'Support Request Detail View':'support/api/v1/supportrequest/view/details/<int:pk>/',
        'Support Request Create':'support/api/v1/supportrequest/create/',
        'Support Request Update':'support/api/v1/supportrequest/update/<int:pk>/',
        'Support Request Delete':'support/api/v1/supportrequest/delete/<int:pk>/',

        'Support Feedback List':'support/api/v1/allsupportfeedback/view',
        'Support Feedback Detail View':'support/api/v1/supportfeedback/view/details/<int:pk>/',
        'Support Feedback Create':'support/api/v1/supportfeedback/create/',
        'Support Feedback Update':'support/api/v1/supportfeedback/update/<int:pk>/',
        'Support Feedback Delete':'support/api/v1/supportfeedback/delete/<int:pk>/',
    }
    return Response(api_endpoints)


class SupportRequestList(generics.ListAPIView):
  queryset = SupportRequest.objects.all()
  serializer_class = SupportRequestSerializer 
  permission_classes = [IsAdminOrReadOnly]


class SupportRequestDetails(generics.RetrieveAPIView):
  queryset = SupportRequest.objects.all()
  serializer_class = SupportRequestSerializer
  permission_classes = [IsAdminOrReadOnly]


class SupportRequestCreate(generics.ListCreateAPIView):
  queryset = SupportRequest.objects.all()
  serializer_class = SupportRequestSerializer
  permission_classes = [permissions.AllowAny]


class SupportRequestUpdate(generics.RetrieveUpdateAPIView):
  queryset = SupportRequest.objects.all()
  serializer_class = SupportRequestSerializer
  permission_classes = [IsOwner]


class SupportRequestDelete(generics.RetrieveDestroyAPIView):
  queryset = SupportRequest.objects.all()
  serializer_class = SupportRequestSerializer
  permission_classes = [IsOwner]



class SupportFeedbackList(generics.ListAPIView):
  queryset = SupportFeedback.objects.all()
  serializer_class = SupportFeedbackSerializer 
  permission_classes = [IsAdminOrReadOnly]


class SupportFeedbackDetails(generics.RetrieveAPIView):
  queryset = SupportFeedback.objects.all()
  serializer_class = SupportFeedbackSerializer
  permission_classes = [IsAdminOrReadOnly]


class SupportFeedbackCreate(generics.ListCreateAPIView):
  queryset = SupportFeedback.objects.all()
  serializer_class = SupportFeedbackSerializer
  permission_classes = [IsAdminOrReadOnly]


class SupportFeedbackUpdate(generics.RetrieveUpdateAPIView):
  queryset = SupportFeedback.objects.all()
  serializer_class = SupportFeedbackSerializer
  permission_classes = [IsOwner]


class SupportFeedbackDelete(generics.RetrieveDestroyAPIView):
  queryset = SupportFeedback.objects.all()
  serializer_class = SupportFeedbackSerializer
  permission_classes = [IsOwner]