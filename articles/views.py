from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from articles.models import ArticlePost, Comment
from .serializers import ArticleSerializer, CommentSerializer
from rest_framework.decorators import api_view
# from utils.permissions import IsOwnerOrReadOnly
# Create your views here.

@api_view(['GET'])
def apiRequest(request):
    api_endpoints = {
        'Articles List':'articles/api/v1/allarticles/view',
        'Article Detail View':'articles/api/v1/article/view/details/<int:pk>/',
        'Article Create':'articles/api/v1/article/create/',
        'Article Update':'articles/api/v1/article/update/<int:pk>/',
        'Article Delete':'articles/api/v1/article/delete/<int:pk>/',

        'Comments List':'articles/api/v1/allcomments/view',
        'Comment Detail View':'articles/api/v1/comment/view/details/<int:pk>/',
        'Comment Create':'articles/api/v1/comment/create/',
        'Comment Update':'articles/api/v1/comment/update/<int:pk>/',
        'Comment Delete':'articles/api/v1/comment/delete/<int:pk>/',
    }
    return Response(api_endpoints)

class ArticleList(generics.ListAPIView):
  queryset = ArticlePost.objects.all()
  serializer_class = ArticleSerializer 
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class ArticleDetails(generics.RetrieveAPIView):
  queryset = ArticlePost.objects.all()
  serializer_class = ArticleSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class ArticleCreate(generics.ListCreateAPIView):
  queryset = ArticlePost.objects.all()
  serializer_class = ArticleSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class ArticleUpdate(generics.RetrieveUpdateAPIView):
  queryset = ArticlePost.objects.all()
  serializer_class = ArticleSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class ArticleDelete(generics.RetrieveDestroyAPIView):
  queryset = ArticlePost.objects.all()
  serializer_class = ArticleSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]



class CommentList(generics.ListAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer 
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class CommentDetails(generics.RetrieveAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class CommentCreate(generics.ListCreateAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class CommentUpdate(generics.RetrieveUpdateAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class CommentDelete(generics.RetrieveDestroyAPIView):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]