from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url
from teziapp import views as app_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
        re_path('^register/',app_views.register,name="register"),
        re_path('^profile/',app_views.profile,name="profile"),
        re_path('^login/',auth_views.LoginView.as_view(template_name='teziapp/login.html'),name='login'),
        re_path('^logout',auth_views.LogoutView.as_view(template_name='teziapp/logout.html'),name='logout'),
    ]
