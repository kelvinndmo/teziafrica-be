from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from datetime import datetime, timedelta
from django.conf import settings
from django.db import models


class UserManager(BaseUserManager):
    """" 
    We need to override the `create_user` method so that users can
    only be created when all non-nullable fields are populated.
    """
    def create_user(self, first_name=None, last_name=None, email=None, password=None, role='TA'):
  
        if not email:
            raise ValueError('Don\'t forget your Email!')
        if not full_name:
            raise TypeError('Users must have a full_name.')
        if not password:
            raise TypeError('Users must have a password.')           
        user = self.model(
            full_name=full_name,
            email=self.normalize_email(email),
            username=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, full_name=None, email=None, password=None):
        """Create a `User` who is also a superuser"""
        if not full_name:
            raise TypeError('Superusers must have a full name.')
        if not email:
            raise TypeError('Superusers must have an email address.')        
        if not password:
            raise TypeError('Superusers must have a password.')
        user = self.model(
            full_name=full_name, 
            email=self.normalize_email(email))
        user.is_admin = True
        user.is_active = True       
        user.set_password(password)
        user.save()
      

class User(AbstractBaseUser):
    """This class define the user model"""
    USER_ROLES = (
        ('TA', 'TEZI ADMIN'),
        ('CA', 'CUSTOMER USER'),
        ('CA', 'CLIENT ADMIN'),
        ('CE', 'CLIENT EMPLOYEE'),
    )
    username = models.CharField(null=True, blank=True, max_length=100, unique=True)
    email = models.EmailField(max_length=162, unique=True)
    role = models.CharField(verbose_name='user role', max_length=2, choices=USER_ROLES,
        default='CU'
    )
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    image = models.ImageField(upload_to='user_images/%Y/%m/%d', default='default.jpg')
    display_name = models.CharField(('display name'), max_length=70, blank=True, null=True, unique=False)
    verified = models.BooleanField(default=False)
    

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name'] # Email & Password are required by default.

    objects = UserManager()

    def __str__(self):
        return f'{self.email}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def __str__(self):
        return f'(self.first_name) (self.last_name)'

    @property
    def token(self):
        return self._generate_jwt_token()

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_verified(self):
        return self.verified


    def _generate_jwt_token(self):  
        token_expiry = datetime.now() + timedelta(hours=24)  

        token = jwt.encode({
            'id': self.pk,
            'email': self.get_email,
            'exp': int(token_expiry.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')


class Client(models.Model):
    """This class defines the client Company Model"""
    
    client_name = models.CharField(max_length=100, unique=True)
    client_admin = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='employer'
    )
    phone = models.CharField(max_length=17, unique=True)
    email = models.EmailField(unique=True)
    address = models.CharField('physical address', max_length=1024,
    )
    objects = models.Manager()
    
    def __str__(self):
        return self.client_name
