from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from .models import Quiz, QuizResponses
from .serializers import QuizSerializer, QuizResponsesSerializer
from rest_framework.decorators import api_view
from drf_multiple_model.views import ObjectMultipleModelAPIView
from drf_multiple_model.pagination import MultipleModelLimitOffsetPagination
# from utils.permissions import IsOwnerOrReadOnly


# Create your views here.

@api_view(['GET'])
def apiRequest(request):
    api_endpoints = {
        'Quizs List':'flowbuilder/api/v1/flowbuilders/view',
        'Quiz Detail View':'flowbuilder/api/v1/flowbuilder/view/details/<int:pk>/',
        'Quiz Create':'flowbuilder/api/v1/flowbuilder/create/',
        'Quiz Update':'flowbuilder/api/v1/flowbuilder/update/<int:pk>/',
        'Quiz Delete':'flowbuilder/api/v1/flowbuilder/delete/<int:pk>/',

        'Quiz Responses List':'flowbuilder/api/v1/flowbuilders/responses/view',
        'Quiz Responses Detail View':'flowbuilder/api/v1/flowbuilder/response/view/details/<int:pk>/',
        'Quiz Responses Create':'flowbuilder/api/v1/flowbuilder/response/create/',
        'Quiz Responses Update':'flowbuilder/api/v1/flowbuilder/response/update/<int:pk>/',
        'Quiz Responses Delete':'flowbuilder/api/v1/flowbuilder/response/delete/<int:pk>/',
        'All FlowBuilder Items': 'flowbuilder/api/v1/flowbuilder/all',
    }
    return Response(api_endpoints)


class QuizList(generics.ListAPIView):
  queryset = Quiz.objects.all()
  serializer_class = QuizSerializer 
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class QuizDetails(generics.RetrieveAPIView):
  queryset = Quiz.objects.all()
  serializer_class = QuizSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class QuizCreate(generics.ListCreateAPIView):
  queryset = Quiz.objects.all()
  serializer_class = QuizSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class QuizUpdate(generics.RetrieveUpdateAPIView):
  queryset = Quiz.objects.all()
  serializer_class = QuizSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class QuizDelete(generics.RetrieveDestroyAPIView):
  queryset = Quiz.objects.all()
  serializer_class = QuizSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]




class QuizResponsesList(generics.ListAPIView):
    queryset = QuizResponses.objects.all()
    serializer_class = QuizResponsesSerializer 
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class QuizResponsesDetails(generics.RetrieveAPIView):
  queryset = QuizResponses.objects.all()
  serializer_class = QuizResponsesSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class QuizResponsesCreate(generics.ListCreateAPIView):
  queryset = QuizResponses.objects.all()
  serializer_class = QuizResponsesSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class QuizResponsesUpdate(generics.RetrieveUpdateAPIView):
  queryset = QuizResponses.objects.all()
  serializer_class = QuizResponsesSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class QuizResponsesDelete(generics.RetrieveDestroyAPIView):
  queryset = QuizResponses.objects.all()
  serializer_class = QuizResponsesSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class LimitPagination(MultipleModelLimitOffsetPagination):
    default_limit = 2

class AllFlowView(ObjectMultipleModelAPIView):
    pagination_class = LimitPagination
    querylist = [
        {'queryset': Quiz.objects.all(), 'serializer_class': QuizSerializer},
        {'queryset': QuizResponses.objects.all(), 'serializer_class': QuizResponsesSerializer},
    ]
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]