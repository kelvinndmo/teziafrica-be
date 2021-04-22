# Create your models here.
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Don\'t forget your Email!')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, password):
        user = self.create_user(
            email,
            full_name=full_name,
            password=password,
        )
        user.is_admin = True
        user.is_seller = True
        user.save(using=self._db)
        return user

# create custom user model with email as unque identifier
class User(AbstractBaseUser):
    email = models.EmailField(max_length=162, unique=True)
    full_name = models.CharField(max_length=252)
    phone_number = models.CharField(max_length=11, blank=True)
    image = models.ImageField(upload_to='user_images/%Y/%m/%d', default='default.jpg')
    verified = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_representative = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    joined = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    
    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_full_name(self):
        return self.full_name
       
    def get_name_from_mail(self):
    	mail = self.email
    	name = mail.strip('@')
    	return name[0]

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_verified(self):
        return self.verified
        
class Client(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField()
    profile_creation_complete = models.BooleanField(default=False)
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

# signal to create Client model on user creation
def Client_create(sender, instance, created, *args, **kwargs):
    if created and instance.email:
        Client.objects.get_or_create(user=instance, email=instance.email)

post_save.connect(Client_create, sender=get_user_model())