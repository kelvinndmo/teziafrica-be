from django.urls import path , include
from django.contrib import admin
from django.contrib.auth import views
from flowbuilder import views


# from flowbuilder import views
from rest_framework import routers, serializers, viewsets


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.ListQuizAPIView.as_view(),name="flowbuilder_list"),
    path("create/", views.CreateQuizAPIView.as_view(),name="flowbuilder_create"),
    path("update/",views.UpdateQuizAPIView.as_view(),name="flowbuilder_update"),
    path("delete/",views.DeleteQuizAPIView.as_view(),name="flowbuilder_delete")
]
