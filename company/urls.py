from django.urls import path , include
from django.contrib import admin
from django.contrib.auth import views
from company import views



from rest_framework import routers, serializers, viewsets


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.ListCompanyAPIView.as_view(),name="company_list"),
    path("create/", views.CreateCompanyAPIView.as_view(),name="company_create"),
    path("update/",views.UpdateCompanyAPIView.as_view(),name="company_update"),
    path("delete/",views.DeleteCompanyAPIView.as_view(),name="company_delete")
]


