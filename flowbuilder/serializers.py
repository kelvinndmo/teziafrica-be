from rest_framework import serializers
from .models import Quiz, QuizResponses


class QuizSerializer(serializers.ModelSerializer):

  class Meta:
    model = Quiz
    fields = ['id','user', 'title']



class QuizResponsesSerializer(serializers.ModelSerializer):

  class Meta:
    model = QuizResponses
    fields = ['id', 'quiz', 'reply', 'author', 'order']