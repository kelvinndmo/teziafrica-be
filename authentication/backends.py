import jwt
from rest_framework import authentication, exceptions
from django.conf import settings
from authentication.models import User

class JWTAuthentication(authentication.BaseAuthentication):

    auth_header_prefix = "Bearer".lower()

    def authenticate(self, request):
        request.user = None

        auth_header = authentication.get_authorization_header(request).split()

        if not auth_header:
            return None
        
        if len(auth_header) == 1:
            return None

         
        if len(auth_header) > 2:
            return None

        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')

        if prefix.lower() == self.auth_header_prefix:
            return None
        
        return self._authenticate_credentials(request, token)

    
    def _authenticate_credentials(self, request, token):

        try:
            payload = jwt.decode(token, settings.SECRET_KEY)

        except jwt.ExpiredSignatureError:
            message = 'Your sesssion has expired, please log in again.'
            raise exceptions.AuthenticationFailed(message)
        except Exception as e:
            message = str(e)
            raise exceptions.AuthenticationFailed(message)

        
        try:
            user = User.objects.get(pk=payload['id'])
        except User.DoesNotExist:
            msg = 'User not found.'
            raise exceptions.AuthenticationFailed(msg)

        if not user.is_active:
            msg = "Your account has been deactivated, please reach out to Tezi support."
            raise exceptions.AuthenticationFailed(msg)
        
        return(user, token)
     
