from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import *

urlpatterns = [
   path('', views.apiRequest, name='flowbuilder'),
   path('api/v1/flowbuilders/view', views.QuizList.as_view(), name='api/v1/flowbuilders/view'),
   path('api/v1/flowbuilder/view/details/<int:pk>/', views.QuizDetails.as_view(), name='api/v1/flowbuilder/view/details'),
   path('api/v1/flowbuilder/update/<int:pk>/', views.QuizUpdate.as_view(), name='api/v1/flowbuilder/update'),
   path('api/v1/flowbuilder/delete/<int:pk>/', views.QuizDelete.as_view(), name='api/v1/flowbuilder/delete'),
   path('api/v1/flowbuilder/create/', views.QuizCreate.as_view(), name='api/v1/flowbuilder/create'),

   path('api/v1/flowbuilders/responses/view', views.QuizResponsesList.as_view(), name='api/v1/flowbuilders/responses/view'),
   path('api/v1/flowbuilder/response/view/details/<int:pk>/', views.QuizResponsesDetails.as_view(), name='api/v1/flowbuilder/response/view/details'),
   path('api/v1/flowbuilder/response/update/<int:pk>/', views.QuizResponsesUpdate.as_view(), name='api/v1/flowbuilder/response/update'),
   path('api/v1/flowbuilder/response/delete/<int:pk>/', views.QuizResponsesDelete.as_view(), name='api/v1/flowbuilder/response/delete'),
   path('api/v1/flowbuilder/response/create/', views.QuizResponsesCreate.as_view(), name='api/v1/flowbuilder/response/create'),
   path('api/v1/flowbuilder/all', views.AllFlowView.as_view(), name='api/v1/flowbuilder/all')
]

urlpatterns = format_suffix_patterns(urlpatterns)