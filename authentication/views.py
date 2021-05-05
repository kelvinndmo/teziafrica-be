from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from authentication.serializers import RegistrationSerializer, LoginSerializer
from django.forms.models import model_to_dict
from django.contrib import messages
from rest_framework import authentication
from django.http import Http404
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from authentication.permissions import (
    IsClientAdmin,
    IsProfileOwner,
    IsOwnerOrAdmin)                                        


class RegistrationAPIView(generics.GenericAPIView):
    """Register new users."""
    serializer_class = RegistrationSerializer
    renderer_classes = (UserJSONRenderer,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
              
        response = {
            "data": {
                "user": dict(user_data),
                "message": "Account created successfully,please check your "
                           "mailbox to activate your account ",
                "status": "success"
            }
        }
        return Response(response, status=status.HTTP_201_CREATED)


class LoginAPIView(generics.GenericAPIView):
    """login a user via email"""
    serializer_class = LoginSerializer
    renderer_classes = (UserJSONRenderer,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.data
        response = {
            "data": {
                "user": dict(user_data),
                "message": "You have successfully logged in",
                "status": "success"
            }
        }
        return Response(response, status=status.HTTP_200_OK)

class ClientCreateView(generics.GenericAPIView, BaseUtils):
    """
    Register new client company by client admin
    """
    serializer_class = ClientSerializer
    renderer_classes = (ClientJSONRenderer,)
    permission_classes = (IsClientAdmin,)

    def get_queryset(self):
        user = self.request.user
        return Client.active_objects.filter(client_admin=user.id)

    def get(self, request):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        if len(serializer.data) == 0:
            response = {
                "data": {
                    "message": "You don't have a client company created"
                }
            }
            status_code = status.HTTP_404_NOT_FOUND
        else:
            response = {
                "data": {
                    "client_company": serializer.data[0],
                    "message": "You have retrieved your client company",
                }
            }
            status_code = status.HTTP_200_OK
        return Response(response, status=status_code)

    """
    Register new client company by client admin
    """

    def post(self, request):
        data = request.data
        if self.check_client_admin_has_company(request.user.id):
            return Response(
                {'error': 'You cannot be admin of more than one client'},
                status.HTTP_403_FORBIDDEN
            )
        data["client_admin"] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        company = serializer.validated_data['client_name']
        admin = serializer.validated_data['client_admin']

        recipient = list(
            User.active_objects.filter(role="TA").values_list('email',
                                                              flat=True))

        send_email_notification.delay(payload)

        response = {
            "client_company": serializer.data,
            "message": "Your request to create a company has been "
                       "received, please wait for approval from landville "
                       "admin."
        }

        return Response(response, status=status.HTTP_201_CREATED)

    @staticmethod
    def check_client_admin_has_company(id_value):
        """
        Checks if client admin admin already has a company
        """
        return bool(Client.active_objects.filter(client_admin_id=id_value))

    def patch(self, request):
        """
        Handle Update a user's company details once created.
        :param request:
        :return: company Details
        """
        data = request.data
        company = self.get_queryset()
        serializer = self.serializer_class(company[0], data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        response = {
            "client_company": serializer.data,
            "message": "Successfully Updated client company details."
        }

        return Response(response, status=status.HTTP_200_OK)

    def delete(self, request):
        """
        Handles deleting a client company
        :param request:
        :return:
        """
        company = self.get_queryset()
        if not company:
            return Response({"errors": "Client Company Does not exist"},
                            status=status.HTTP_404_NOT_FOUND)
        company[0].delete()
        return Response("Company Deleted Successfully", status.HTTP_200_OK)


class ClientListView(generics.GenericAPIView):
    """
    Return a list of registered clients
    """
    serializer_class = ClientSerializer
    renderer_classes = (ClientJSONRenderer,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """ Returns all active client companies  """

        return Client.active_objects.all_approved()

    def get(self, request):
        """ Handles retrieving all existing client companies """

        serializer = self.serializer_class(self.get_queryset(), many=True)
        if not serializer.data:
            response = {
                "message": "There are no clients at the moment."
            }
            status_code = status.HTTP_404_NOT_FOUND
        else:
            response = {
                "client_companies": serializer.data,
                "message": "You have retrieved all clients",
            }
            status_code = status.HTTP_200_OK
        return Response(response, status=status_code)


class LogoutView(generics.CreateAPIView):
    """
    This class deals with logging out a user by
    creating blacklist tokens
    """
    serializer_class = LoginSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, **args):
        """
        This method creates a blacklist token
        """

        auth_header = authentication.get_authorization_header(request).split()
        token = auth_header[1].decode('utf-8')
        data = {'token': token}

        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data


        return Response(
            {
                'data':
                    {"message": "Successfully logged out"}
            },
            status=status.HTTP_200_OK
        )


