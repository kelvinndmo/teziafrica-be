from rest_framework.routers import DefaultRouter
from django.urls import path,re_path,include
from . import views
from .views import *
from .views import LoginAPI
from django.urls import path
from knox.views import LoginView as KnoxLoginView

userSignup=UserViewSet.as_view({
    'get':'list',
    'post':'create'
})

userLogin=UserViewSet.as_view({
    'get':'list',
    'post':'list'
})

userDetail=UserViewSet.as_view({
    'get':'retrieve'
})

router = DefaultRouter()
router.register(r'User', UserViewSet)
router.register(r'Profile', ProfileViewSet)
router.register(r'Client', ClientViewSet)

urlpatterns =[
    path('', views.home, name='index'),
    path('auth/signup/', userSignup, name='user_signup'),
    path('auth/login/', userLogin, name='user_login'),
    path('users/<int:pk>/', userDetail, name='user-detail'),
]