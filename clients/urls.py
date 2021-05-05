from django.urls import path
from clients.views import CreateListClientAPIView

urlpatterns = [
    path('', CreateListClientAPIView.as_view(), name ='clients')
]
