from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.db import models
# from django.core.serializer.json import DjangoJSONEncoder

class UserManager(BaseUserManager):
    """" 
    We need to override the `create_user` method so that users can
    only be created when all non-nullable fields are populated.
    """
    def create_user(self, email, full_name, password=None):
  
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
        # user.is_verified = True
        user.set_password(password)
        user.save()
      

class User(AbstractBaseUser):
    email = models.EmailField(max_length=162, unique=True)
    full_name = models.CharField(max_length=252, blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    image = models.ImageField(upload_to='user_images/%Y/%m/%d', default='default.jpg')
    display_name = models.CharField(('display name'), max_length=70, blank=True, null=True, unique=False)
    verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_representative = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    joined = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name',] # Email & Password are required by default.

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_full_name(self):
        return self.full_name

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_verified(self):
        return self.verified

class Client(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(unique=True)
    # address = JSONField(
    #     verbose_name='physical address', encoder=DjangoJSONEncoder
    # )
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.email)

class Guest(models.Model):
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.email)

def client_create(sender, instance, created, *args, **kwargs):
    if created and instance.email:
        Client.objects.get_or_create(user=instance, email=instance.email)

post_save.connect(client_create, sender=get_user_model())

