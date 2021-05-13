from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import *


urlpatterns = [
    path('', views.apiRequest, name="authentication"),
    path('register/', views.RegistrationAPIView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('api/v1/allprofiles/view/', views.UserList.as_view(), name='api/v1/allprofiles/view'),
    path('api/v1/profile/view/details/<int:pk>/', views.UserDetails.as_view(), name='api/v1/profile/view/details'),
    path('api/v1/profile/update/<int:pk>/', views.UserUpdate.as_view(), name='api/v1/profile/update'),
    path('api/v1/profile/delete/<int:pk>/', views.UserDelete.as_view(), name='api/v1/profile/delete'),
    path('api/v1/profile/create/', views.UserCreate.as_view(), name='api/v1/profile/create'),

    path('api/v1/allcompanies/view/', views.CompanyList.as_view(), name='api/v1/allcompanies/view'),
    path('api/v1/company/view/details/<int:pk>/', views.CompanyDetails.as_view(), name='api/v1/company/view/details'),
    path('api/v1/company/update/<int:pk>/', views.CompanyUpdate.as_view(), name='api/v1/company/update'),
    path('api/v1/company/delete/<int:pk>/', views.CompanyDelete.as_view(), name='api/v1/company/delete'),
    path('api/v1/company/create/', views.CompanyCreate.as_view(), name='api/v1/company/create')
]

urlpatterns = format_suffix_patterns(urlpatterns)