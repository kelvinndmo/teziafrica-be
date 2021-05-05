from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from flowbuilder.serializers import QuizSerializer , QuizResponseSerializer
from flowbuilder.models import Quiz , QuizResponses
from rest_framework.views import APIView
from django.contrib.auth.models import User


# Quiz APIView

class ListQuizAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = QuizSerializer


class CreateQuizAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = QuizSerializer

class UpdateQuizAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = QuizSerializer

class DeleteQuizAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = QuizSerializer
   
# QuizResponses APIView

class ListQuizResponsesAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = QuizResponseSerializer


class CreateQuizResponsesAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = QuizResponseSerializer

class UpdateQuizResponsesAPIView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = QuizResponseSerializer

class DeleteQuizResponsesAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = QuizResponseSerializer
