from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import *

urlpatterns = [
   path('', views.apiRequest, name='support'),
   path('api/v1/allsupportrequests/view', views.SupportRequestList.as_view(), name='api/v1/allsupportrequests/view'),
   path('api/v1/supportrequest/view/details/<int:pk>/', views.SupportRequestDetails.as_view(), name='api/v1/supportrequest/view/details'),
   path('api/v1/supportrequest/update/<int:pk>/', views.SupportRequestUpdate.as_view(), name='api/v1/supportrequest/update'),
   path('api/v1/supportrequest/delete/<int:pk>/', views.SupportRequestDelete.as_view(), name='api/v1/supportrequest/delete'),
   path('api/v1/supportrequest/create/', views.SupportRequestCreate.as_view(), name='api/v1/supportrequest/create'),

   path('api/v1/allsupportfeedback/view', views.SupportFeedbackList.as_view(), name='support/api/v1/allsupportfeedback/view'),
   path('api/v1/supportfeedback/view/details/<int:pk>/', views.SupportFeedbackDetails.as_view(), name='api/v1/supportfeedback/view/details'),
   path('api/v1/supportfeedback/update/<int:pk>/', views.SupportFeedbackUpdate.as_view(), name='api/v1/supportfeedback/update'),
   path('api/v1/supportfeedback/delete/<int:pk>/', views.SupportFeedbackDelete.as_view(), name='api/v1/supportfeedback/delete'),
   path('api/v1/supportfeedback/create/', views.SupportFeedbackCreate.as_view(), name='api/v1/supportfeedback/create'),
]

urlpatterns = format_suffix_patterns(urlpatterns)