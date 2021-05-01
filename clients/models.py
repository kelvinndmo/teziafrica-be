from django.db import models
from django.contrib.auth import get_user_model

class Organization(models.Model):
    name = models.CharField(max_length=90, unique=True)
    description = models.TextField()
    manager = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        blank=True
    )

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=90)
    description = models.TextField()
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='organization_name',
        blank=True
    )
    manager = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        related_name='manager',
        null=True
    )

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='department_name'
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name='organization'
    )

    def __str__(self):
        return user.full_name
class BaseAbstractModel(models.Model):
    """
    This model defines base models that implements common fields like:
    created_at
    updated_at
    is_deleted
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    def soft_delete(self):
        """Soft delete a model instance"""
        self.is_deleted = True
        self.save()

    class Meta:
        abstract = True
        ordering = ['-created_at']
