from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from .models import ChatInput, ChatOutPut
from .serializers import ChatInputSerializer, ChatOutPutSerializer
from rest_framework.decorators import api_view
from drf_multiple_model.views import ObjectMultipleModelAPIView
from drf_multiple_model.pagination import MultipleModelLimitOffsetPagination
# from utils.permissions import IsOwnerOrReadOnly


# Create your views here.

@api_view(['GET'])
def apiRequest(request):
    api_endpoints = {
        'ChatInput List':'flowbuilder/api/v1/flowbuilders/view',
        'ChatInput Detail View':'flowbuilder/api/v1/flowbuilder/view/details/<int:pk>/',
        'ChatInput Create':'flowbuilder/api/v1/flowbuilder/create/',
        'ChatInput Update':'flowbuilder/api/v1/flowbuilder/update/<int:pk>/',
        'ChatInput Delete':'flowbuilder/api/v1/flowbuilder/delete/<int:pk>/',

        'ChatOutPut List':'flowbuilder/api/v1/flowbuilders/responses/view',
        'ChatOutPut Detail View':'flowbuilder/api/v1/flowbuilder/response/view/details/<int:pk>/',
        'ChatOutPut Create':'flowbuilder/api/v1/flowbuilder/response/create/',
        'ChatOutPut Update':'flowbuilder/api/v1/flowbuilder/response/update/<int:pk>/',
        'ChatOutPut Delete':'flowbuilder/api/v1/flowbuilder/response/delete/<int:pk>/',
        'All FlowBuilder Items': 'flowbuilder/api/v1/flowbuilder/all',
    }
    return Response(api_endpoints)


class ChatInputList(generics.ListAPIView):
  queryset = ChatInput.objects.all()
  serializer_class = ChatInputSerializer 
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class ChatInputDetails(generics.RetrieveAPIView):
  queryset = ChatInput.objects.all()
  serializer_class = ChatInputSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class ChatInputCreate(generics.ListCreateAPIView):
  queryset = ChatInput.objects.all()
  serializer_class = ChatInputSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class ChatInputUpdate(generics.RetrieveUpdateAPIView):
  queryset = ChatInput.objects.all()
  serializer_class = ChatInputSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class ChatInputDelete(generics.RetrieveDestroyAPIView):
  queryset = ChatInput.objects.all()
  serializer_class = ChatInputSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]




class ChatOutPutList(generics.ListAPIView):
    queryset = ChatOutPut.objects.all()
    serializer_class = ChatOutPutSerializer 
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class ChatOutPutDetails(generics.RetrieveAPIView):
  queryset = ChatOutPut.objects.all()
  serializer_class = ChatOutPutSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class ChatOutPutCreate(generics.ListCreateAPIView):
  queryset = ChatOutPut.objects.all()
  serializer_class = ChatOutPutSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class ChatOutPutUpdate(generics.RetrieveUpdateAPIView):
  queryset = ChatOutPut.objects.all()
  serializer_class = ChatOutPutSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class ChatOutPutDelete(generics.RetrieveDestroyAPIView):
  queryset = ChatOutPut.objects.all()
  serializer_class = ChatOutPutSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class LimitPagination(MultipleModelLimitOffsetPagination):
    default_limit = 2

class AllFlowView(ObjectMultipleModelAPIView):
    serializer_class = ChatInputSerializer
    pagination_class = LimitPagination
    querylist = [
        {'queryset': ChatInput.objects.all(), 'serializer_class': ChatInputSerializer},
        {'queryset': ChatOutPut.objects.all(), 'serializer_class': ChatOutPutSerializer},
    ]
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]