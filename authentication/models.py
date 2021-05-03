from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.mail import send_mail
from django.contrib.auth.base_user import BaseUserManager


# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):

    CUSTOMER = 1
    CLIENT = 2
    ADMIN = 3
    GUEST = 4
    QUIZ = 5
    QUIZRESPONSE = 6
    ROLE_CHOICES = (
        (CUSTOMER, 'customer'),
        (CLIENT, 'client'),
        (ADMIN, 'admin'),
        (GUEST, 'guest'),
        (QUIZ, 'quiz'),
        (QUIZRESPONSE, 'quizresponse'),
    )

