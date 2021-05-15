from rest_framework import serializers
from authentication.models import User, Company, Staff
from rest_framework.authentication import authenticate

class RegisterationSerializer(serializers.ModelSerializer):

  first_name = serializers.CharField()
  last_name = serializers.CharField()

  role = serializers.ChoiceField(choices=[('AD', 'TEZI ADMIN'),
        ('CO', 'COMPANY'),
        ('ST', 'STAFF'),
        ('CL', 'CLIENT')])
        
  password = serializers.CharField(min_length=8,
  write_only=True,
  error_messages={
    "min_length": "Password should be at least 8 characters"
      }
  )

  class Meta:
    model = User
    fields = ['email', 'first_name', 'last_name', 'role', 'password']

  def create(self, validate_data):
    user=User.objects.create(**validate_data)
    return user 


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['email', 'first_name', 'last_name', 'role', 'password']


class CompanySerializer(serializers.ModelSerializer):
  class Meta:
    model = Company
    fields = ['approval_status', 'company_name', 'company_admin', 'phone', 'image', 'email', 'address', 'industry']


class StaffSerializer(serializers.ModelSerializer):
  class Meta:
    model = Staff
    fields = ['approval_status', 'staff_name', 'staff_company', 'image', 'phone', 'email', 'address']

 
class LoginSerializer(serializers.Serializer):
  email = serializers.EmailField()
  password = serializers.CharField(max_length=128, write_only=True)
  token = serializers.CharField(read_only=True)
  role = serializers.CharField(read_only=True)

  def validate(self, data):
    email = data.get("email", None)
    password = data.get("password", None)

    user = authenticate(username=email, password=password)

    if user is None:
      raise serializers.ValidationError({
        'invalid':'wrong email and password'
      })
    
    user = {
      "email":user.email,
      "token":user.token,
      "role":user.role
    }
    
    return user

  class Meta:
    model = User
    fields = ['email', 'token', 'role', 'password']