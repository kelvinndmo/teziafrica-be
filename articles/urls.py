from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import *

urlpatterns = [
   path('', views.apiRequest, name='articles'),
   path('api/v1/allarticles/view', views.ArticleList.as_view(), name='api/v1/allarticles/view'),
   path('api/v1/article/view/details/<int:pk>/', views.ArticleDetails.as_view(), name='api/v1/article/view/details'),
   path('api/v1/article/update/<int:pk>/', views.ArticleUpdate.as_view(), name='api/v1/article/update'),
   path('api/v1/article/delete/<int:pk>/', views.ArticleDelete.as_view(), name='api/v1/article/delete'),
   path('api/v1/article/create/', views.ArticleCreate.as_view(), name='api/v1/article/create'),

   path('api/v1/allcomments/view', views.CommentList.as_view(), name='api/v1/allcomments/view'),
   path('api/v1/comment/view/details/<int:pk>/', views.CommentDetails.as_view(), name='api/v1/comment/view/details'),
   path('api/v1/comment/update/<int:pk>/', views.CommentUpdate.as_view(), name='api/v1/comment/update'),
   path('api/v1/comment/delete/<int:pk>/', views.CommentDelete.as_view(), name='api/v1/comment/delete'),
   path('api/v1/comment/create/', views.CommentCreate.as_view(), name='api/v1/comment/create'),
]

urlpatterns = format_suffix_patterns(urlpatterns)