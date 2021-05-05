from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from tickets.models import Ticket, Feedback
from .serializers import TicketSerializer, FeedbackSerializer
from rest_framework.decorators import api_view
# from utils.permissions import IsOwnerOrReadOnly
# Create your views here.

@api_view(['GET'])
def apiRequest(request):
    api_endpoints = {
        'Ticket List':'tickets/api/v1/alltickets/view',
        'Ticket Detail View':'ticket/api/v1/ticket/view/details/<int:pk>/',
        'Ticket Create':'ticket/api/v1/ticket/create/',
        'Ticket Update':'ticket/api/v1/ticket/update/<int:pk>/',
        'Ticket Delete':'ticket/api/v1/ticket/delete/<int:pk>/',

        'Feedback List':'tickets/feedback/api/v1/allfeedback/view',
        'Feedback Detail View':'ticket/feedback/api/v1/feedback/view/details/<int:pk>/',
        'Feedback Create':'ticket/feedback/api/v1/feedback/create/',
        'Feedback Update':'ticket/feedback/api/v1/feedback/update/<int:pk>/',
        'Feedback Delete':'ticket/feedback/api/v1/feedback/delete/<int:pk>/',
    }
    return Response(api_endpoints)

class TicketList(generics.ListAPIView):
  queryset = Ticket.objects.all()
  serializer_class = TicketSerializer 
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class TicketDetails(generics.RetrieveAPIView):
  queryset = Ticket.objects.all()
  serializer_class = TicketSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class TicketCreate(generics.ListCreateAPIView):
  queryset = Ticket.objects.all()
  serializer_class = TicketSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class TicketUpdate(generics.RetrieveUpdateAPIView):
  queryset = Ticket.objects.all()
  serializer_class = TicketSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class TicketDelete(generics.RetrieveDestroyAPIView):
  queryset = Ticket.objects.all()
  serializer_class = TicketSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]



class FeedbackList(generics.ListAPIView):
  queryset = Feedback.objects.all()
  serializer_class = FeedbackSerializer 
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class FeedbackDetails(generics.RetrieveAPIView):
  queryset = Feedback.objects.all()
  serializer_class = FeedbackSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class FeedbackCreate(generics.ListCreateAPIView):
  queryset = Feedback.objects.all()
  serializer_class = FeedbackSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class FeedbackUpdate(generics.RetrieveUpdateAPIView):
  queryset = Feedback.objects.all()
  serializer_class = FeedbackSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class FeedbackDelete(generics.RetrieveDestroyAPIView):
  queryset = Feedback.objects.all()
  serializer_class = FeedbackSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]