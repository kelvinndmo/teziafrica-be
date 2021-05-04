from rest_framework import serializers
from flowbuilder.models import Quiz , QuizResponses

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = "__all__"

class QuizResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizResponses
        fields = "__all__"

