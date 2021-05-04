from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Company(models.Model):
    INDUSTRY_CHOICES=[
        ('entertainment', 'Entertainment'),
        ('manufacturing', 'Manufactiring'),
        ('real_estate', 'Real_estate'),
        ('accommodation services', 'Accommodation services'),
        ('financial and insurance', 'Financial and Insurance'),
        ('information and communication', 'Information and Communication'),
    ]
    company_name = models.CharField(max_length=60)
    company_email = models.EmailField(max_length=200, unique=True)
    company_admin = models.ForeignKey(User, on_delete=models.CASCADE)
    adress = models.CharField(max_length=200)
    phone_number = models.CharField(null=True, blank=True, max_length=20)
    industry = models.CharField(max_length=100, choices=INDUSTRY_CHOICES)

    def __str__(self):
        return self.company_name

    def save_company(self):
        self.save()

    def delete_company(self):
        self.delete()