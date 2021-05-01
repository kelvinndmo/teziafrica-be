from django.contrib import admin
from django.contrib.admin import AdminSite

from .models import User, Client

AdminSite.site_title = 'Tezi Admin'
AdminSite.site_header = 'Tezi Admin Panel'

admin.site.register(User)
admin.site.register(Client)