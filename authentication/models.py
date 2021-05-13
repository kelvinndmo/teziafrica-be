from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from datetime import datetime, timedelta
import jwt
from django.conf import settings
from utils.models import BaseAbstractModel
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.postgres.fields import JSONField
# Create your models here.

class UserManager(BaseUserManager):
    def create(self, first_name=None, last_name=None, email=None, password=None, role="CL"):
        if not first_name:
            raise TypeError('Users must have a first name.')

        if not last_name:
            raise TypeError('Users must have a last name.')

        if not email:
            raise TypeError('Users must have an email address.')

        if not password:
            raise TypeError('Users must have a password.')
        

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            username=self.normalize_email(email)
        )

        user.set_password(password)
        # import pdb; pdb.set_trace()
        user.role = role
        user.save()
        return user


    def create_superuser(self, first_name=None, last_name=None, email=None, password=None):
        if not first_name:
            raise TypeError('Users must have a first name.')

        if not last_name:
            raise TypeError('Users must have a last name.')

        if not email:
            raise TypeError('Users must have an email address.')

        if not password:
            raise TypeError('Users must have a password.')
        

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=self.normalize_email(email),
            role='AD'
        )

        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.set_password(password)
        user.save()
        return user


class User(AbstractUser):

    USER_ROLES = (
        ('AD', 'TEZI ADMIN'),
        ('CO', 'COMPANY'),
        ('ST', 'STAFF'),
        ('CL', 'CLIENT')
    )

    username = models.CharField(null=True, blank=True, max_length=100, unique=True)
    email = models.EmailField(unique=True)
    role = models.CharField(verbose_name="user_role", max_length=2, choices=USER_ROLES, default='CL')

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        token_expiry = datetime.now() + timedelta(hours=24)

        token = jwt.encode({
            'id': self.pk,
            'email': self.email,
            'exp':int(token_expiry.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token


class Company(BaseAbstractModel):
    """This class defines the Company Model"""

    APPROVAL_STATUS = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('revoked', 'Revoked'),
    ]

    INDUSTRY_CHOICES=[
        ('entertainment', 'Entertainment'),
        ('manufacturing', 'Manufactiring'),
        ('real_estate', 'Real_estate'),
        ('accommodation services', 'Accommodation services'),
        ('financial and insurance', 'Financial and Insurance'),
        ('information and communication', 'Information and Communication'),
    ]


    approval_status = models.CharField(
        max_length=10, choices=APPROVAL_STATUS, default='pending')

    company_name = models.CharField(max_length=100, unique=True)
    company_admin = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='employer'
    )
    phone = models.CharField(max_length=17, unique=True)
    email = models.EmailField(unique=True)
    address = JSONField(
        verbose_name='physical address', encoder=DjangoJSONEncoder
    )
    industry = models.CharField(max_length=100, choices=INDUSTRY_CHOICES, default='information and communication')

    def __str__(self):
        return self.company_name