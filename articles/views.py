from django.shortcuts import render
from rest_framework import generics, mixins, status, permissions
from rest_framework.response import Response
from articles.models import ArticlePost, Comment
from .serializers import ArticleSerializer, CommentSerializer
from rest_framework.decorators import api_view
from utils.permissions import IsTeziAdmin, PostUserWritePermissions
from rest_framework.permissions import BasePermission, IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, SAFE_METHODS, IsAuthenticatedOrReadOnly

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
  permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
  queryset = ArticlePost.objects.all()
  serializer_class = ArticleSerializer 
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class ArticleDetails(generics.RetrieveAPIView, PostUserWritePermissions):
  permission_classes = [PostUserWritePermissions]
  queryset = ArticlePost.objects.all()
  serializer_class = ArticleSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class ArticleCreate(generics.ListCreateAPIView, PostUserWritePermissions):
  permission_classes = [PostUserWritePermissions,]
  queryset = ArticlePost.objects.all()
  serializer_class = ArticleSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class ArticleUpdate(generics.RetrieveUpdateAPIView, PostUserWritePermissions):
  permission_classes = [PostUserWritePermissions]
  queryset = ArticlePost.objects.all()
  serializer_class = ArticleSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class ArticleDelete(generics.RetrieveDestroyAPIView, PostUserWritePermissions):
  permission_classes = [PostUserWritePermissions]
  queryset = ArticlePost.objects.all()
  serializer_class = ArticleSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]



class CommentList(generics.ListAPIView):
  permission_classes = [DjangoModelPermissionsOrAnonReadOnly()]
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer 
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class CommentDetails(generics.RetrieveAPIView):
  permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

class CommentCreate(generics.ListCreateAPIView, PostUserWritePermissions):
  permission_classes = [PostUserWritePermissions]
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class CommentUpdate(generics.RetrieveUpdateAPIView, PostUserWritePermissions):
  permission_classes = [PostUserWritePermissions]
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class CommentDelete(generics.RetrieveDestroyAPIView, PostUserWritePermissions):
  permission_classes = [PostUserWritePermissions]
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  #permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]