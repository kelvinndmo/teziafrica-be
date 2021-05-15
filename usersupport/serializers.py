from rest_framework import serializers
from .models import SupportRequest, SupportFeedback


class SupportRequestSerializer (serializers.ModelSerializer):

  class Meta:
    model = SupportRequest
    fields = ['id', 'title', 'post', 'date_posted', 'screenshot', 'author']




class SupportFeedbackSerializer(serializers.ModelSerializer):

  class Meta:
    model = SupportFeedback
    fields = ['id', 'body', 'post', 'screenshot', 'author', 'date_posted']