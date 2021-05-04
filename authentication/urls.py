from django.urls import path
# from authentication.views  import RegistrationAPIView
from .views import *

app_name = 'authentication'

urlpatterns = [
    # path('register/', RegistrationAPIView.as_view(), name='register'),
]
