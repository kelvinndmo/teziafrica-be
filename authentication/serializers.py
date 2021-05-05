from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers
from rest_framework.authentication import authenticate
from authentication.models import User
from authentication.serializers import RegistrationSerializer, LoginSerializer


class RegistrationSerializer(serializers.ModelSerializer):
    """Serialize registration requests and create a new user."""

    first_name = serializers.CharField() 
    last_name = serializers.CharField() 
    role = serializers.ChoiceField(choices*[('TA', 'TEZI ADMIN'),
        ('CA', 'CUSTOMER USER'),
        ('CA', 'CLIENT ADMIN'),
        ('CE', 'CLIENT EMPLOYEE'),])   


    password = serializers.CharField(
        max_length=128,
        min_length=6,
        write_only=True,
        error_messages={
            "min_length": "Password should be at least {min_length} characters"
        }
    )

    class Meta:
        model = User
        fields = ["email", "fist_name", "role", 
                  "password", "image"]


    def create(self, validated_data):
        """Create a user."""
        del validated_data["confirmed_password"]
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        max_length=128, min_length=6, write_only=True, )
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(username=email, password=password)
        if user is None:
            raise serializers.ValidationError({
                "invalid": "invalid email and password combination"
            })
        if not user.is_verified:
            raise serializers.ValidationError({
                "user": "Your email is not verified,please vist your mail box"
            } )
        user = {
            "email": user.email,
            "token": user.token,
            "role": user.role
        }
        return user

class LoginAPIview(generics.CreateAPIview):
    serializers_class = LoginSerializer
 

    def post(self, request):
        serializers = self.serializers_class(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()

        response = {
            "user":dict(user_data),
            "message":"Account created successfully"
        }

        user_data = serializers.data
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(username=email, password=password)
        if user is None:
            raise serializers.ValidationError({
                "invalid": "invalid email and password combination"
            })
        if not user.is_verified:
            raise serializers.ValidationError({
                "user": "Your email is not verified,please vist your mail box"
            })
        user = {
            "email": user.email,
            "token": user.token,
            "role": user.role
        }
        return user


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'client_name', 'phone', 'email', 
                  'client_admin']
        read_only_fields = ('is_deleted', 'is_published', 'id')

    def validate(self, data):
        """Validate data before it gets saved."""
        phone = data.get("phone")
        address = data.get("address")
        self.validate_phone_number(phone)        
        self.validate_data_instance(
            address, dict,
            {
                "address": "Company address should contain country, City and\
                    Street"
            })

        keys = ["Country", "Street", "City"]
        for key in keys:
            self.validate_dictionary_keys(key, address, {
                "address": "{} is required in address".format(key)
            })

            self.validate_data_instance(address[key], str, {
                "address": "{} must be a string".format(key)
            })
            self.validate_empty_input(key, address, {
                "address": "{} value can not be empty".format(key)
            })

        return data





