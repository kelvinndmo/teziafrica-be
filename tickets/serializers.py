from rest_framework import serializers
from .models import Ticket, Feedback


class TicketSerializer(serializers.ModelSerializer):

  class Meta:
    model = Ticket
    fields = ['id', 'title', 'post', 'date_posted', 'screenshot', 'author']




class FeedbackSerializer(serializers.ModelSerializer):

  class Meta:
    model = Feedback
    fields = ['id', 'body', 'post', 'screenshot', 'author', 'date_posted']