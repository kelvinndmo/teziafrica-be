from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import *

urlpatterns = [
   path('', views.apiRequest, name='tickets'),
   path('tickets/api/v1/alltickets/view', views.TicketList.as_view(), name='tickets/api/v1/alltickets/view'),
   path('ticket/api/v1/ticket/view/details/<int:pk>/', views.TicketDetails.as_view(), name='ticket/api/v1/ticket/view/details'),
   path('ticket/api/v1/ticket/update/<int:pk>/', views.TicketUpdate.as_view(), name='ticket/api/v1/ticket/update'),
   path('ticket/api/v1/ticket/delete/<int:pk>/', views.TicketDelete.as_view(), name='ticket/api/v1/ticket/delete'),
   path('ticket/api/v1/ticket/create/', views.TicketCreate.as_view(), name='ticket/api/v1/ticket/create'),

   path('tickets/feedback/api/v1/allfeedback/view', views.FeedbackList.as_view(), name='tickets/feedback/api/v1/allfeedback/view'),
   path('ticket/feedback/api/v1/feedback/view/details/<int:pk>/', views.FeedbackDetails.as_view(), name='ticket/feedback/api/v1/feedback/view/details'),
   path('ticket/feedback/api/v1/feedback/update/<int:pk>/', views.FeedbackUpdate.as_view(), name='ticket/feedback/api/v1/feedback/update'),
   path('ticket/feedback/api/v1/feedback/delete/<int:pk>/', views.FeedbackDelete.as_view(), name='ticket/feedback/api/v1/feedback/delete'),
   path('ticket/feedback/api/v1/feedback/create/', views.FeedbackCreate.as_view(), name='ticket/feedback/api/v1/feedback/create'),
]

urlpatterns = format_suffix_patterns(urlpatterns)