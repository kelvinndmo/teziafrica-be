from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import serializers

from authentication.models import (
    User, Client, UserProfile,
)
from authentication.signals import SocialAuthProfileUpdate
from authentication.socialvalidators import SocialValidation
from authentication.validators import validate_phone_number
from property.validators import validate_address
from utils import BaseUtils
from clients.password_generator import randomStringwithDigitsAndSymbols
from clients.resethandler import ResetHandler


class RegistrationSerializer(serializers.ModelSerializer):
    """Serialize registration requests and create a new user."""

    full_name = serializers.CharField()    
    image = serializers.CharField(read_only=True, source='userprofile.image')

    password = serializers.CharField(
        max_length=128,
        min_length=6,
        write_only=True,
        error_messages={
            "min_length": "Password should be at least {min_length} characters"
        }
    )
    confirmed_password = serializers.CharField(
        max_length=128,
        min_length=6,
        write_only=True,
        error_messages={
            "min_length": "Password should be at least {min_length} characters"
        }
    )

    class Meta:
        model = User
        fields = ["email", "full_name", 
                  "password", "confirmed_password", "image"]

    def validate(self, data):
        """Validate data before it gets saved."""

        confirmed_password = data.get("confirmed_password")
        try:
            validate_password(data["password"])
        except ValidationError as identifier:
            raise serializers.ValidationError({
                "password": str(identifier).replace(
                    "["", "").replace(""]", "")})

        if not self.do_passwords_match(data["password"], confirmed_password):
            raise serializers.ValidationError({
                "passwords": ("Passwords do not match")
            })

        return data

    def create(self, validated_data):
        """Create a user."""
        del validated_data["confirmed_password"]
        return User.objects.create_user(**validated_data)

    def do_passwords_match(self, password1, password2):
        """Check if passwords match."""
        return password1 == password2


class GoogleAuthSerializer(serializers.Serializer):
    """
    Handle serialization and deserialization of User objects
    """

    access_token = serializers.CharField()

    def validate(self, data):
        """
        Handles validating a request and decoding and getting user's info
        associated to an account on Google then authenticates the User
        : params access_token:
        : return: user_token
        """
        id_info = SocialValidation.google_auth_validation(
            access_token=data.get('access_token'))        
        if not id_info:
            raise serializers.ValidationError('token is not valid')
        
        user_id = id_info['sub']        
        user = User.objects.filter(email=id_info.get('email'))
        if user:
            return {
                'token': user[0].token,
                'user_exists': True,
                'message': 'Welcome back ' + id_info.get('name')
            }

        if id_info.get('picture'):
            id_info['user_profile_picture'] = id_info['picture']        
        SocialAuthProfileUpdate.get_user_info(id_info)

        full_name = id_info.get('name').split()
        full_name = full_name[0]        
        payload = {
            'email': id_info.get('email'),
            'full_name': full_name,            
            'password': randomStringwithDigitsAndSymbols()
        }

        new_user = User.objects.create_user(**payload)
        new_user.is_verified = True

        new_user.social_id = user_id
        new_user.save()

        return {
            'token': new_user.token,
            'user_exists': False,
            'message': 'Welcome to landville. ' + ful_name +
                       '. Ensure to edit your profile.'
        }


class FacebookAuthAPISerializer(serializers.Serializer):
    """Handles serialization and deserialization of User objects."""

    access_token = serializers.CharField()

    def validate(self, data):
        """
        Handles validating the request token by decoding and getting
        user_info associated
        To an account on facebook.
        Then authenticate the user.
        : param access_token:
        : return: user_token
        """
        id_info = SocialValidation.facebook_auth_validation(
            access_token=data.get('access_token'))
        
        if not id_info:
            raise serializers.ValidationError('Token is not valid.')
       
        user_id = id_info['id']
      
        user = User.objects.filter(email=id_info.get('email'))
        if user:
            return {
                'token': user[0].token,
                'user_exists': True,
                'message': 'Welcome back ' + id_info.get('full_name')
            }

       
        if id_info.get('picture'):
            id_info['user_profile_picture'] = id_info[
                'picture']['data']['url']

        SocialAuthProfileUpdate.get_user_info(id_info)

        full_name = id_info.get('full_name')        
        payload = {
            'email': id_info.get('email'),
            'full_name': full_name,           
            'password': randomStringwithDigitsAndSymbols()
        }

        new_user = User.objects.create_user(**payload)
        new_user.is_verified = True
        new_user.social_id = user_id
        new_user.save()

        return {
            'token': new_user.token,
            'user_exists': False,
            'message': 'Welcome to landville. ' + first_name +
                       '. Ensure to edit your profile.'
        }


class TwitterAuthAPISerializer(serializers.Serializer):
    """Handles serialization and deserialization of User objects."""

    access_token = serializers.CharField()
    access_token_secret = serializers.CharField()

    def validate(self, data):
        """
        Handles validating the request token by decoding
        and getting user_info associated
        To an account on twitter.
        Then authenticate the user.
        : param data:
        : return: user_token
        """
        id_info = SocialValidation.twitter_auth_validation(
            access_token=data.get('access_token'),
            access_token_secret=data.get('access_token_secret'))
        
        if 'errors' in id_info:
            raise serializers.ValidationError(
                id_info.get('errors')[0]['message'])       

        user_id = id_info['id_str']
        user = User.objects.filter(email=id_info.get('email'))
        
        if user:
            return {
                'token': user[0].token,
                'user_exists': True,
                'message': 'Welcome back ' + id_info.get('name')
            }

        if id_info.get('profile_image_url_https'):
            profile_url_key = 'profile_image_url_https'
            id_info['user_profile_picture'] = id_info[profile_url_key]

        SocialAuthProfileUpdate.get_user_info(id_info)
    
        full_name = id_info.get('name').split()
        full_name = full_name[0]        
        payload = {
            'email': id_info.get('email'),
            'full_name': full_name,            
            'password': randomStringwithDigitsAndSymbols()
        }

        try:
            new_user = User.objects.create_user(**payload)
            new_user.is_verified = True
            new_user.social_id = user_id
            new_user.save()
        except ValidationError:
            raise serializers.ValidationError('Error While creating User.')

        return {
            'token': new_user.token,
            'user_exists': False,
            'message': 'Welcome to landville. ' + first_name +
                       '. Ensure to edit your profile.'
        }


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
            })
        user = {
            "email": user.email,
            "token": user.token
        }
        return user


class ClientSerializer(serializers.ModelSerializer, BaseUtils):
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





