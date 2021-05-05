from rest_framework import serializers
from .models import Ticket, Feedback


class TicketSerializer(serializers.ModelSerializer):

  class Meta:
    model = Ticket
    fields = ['id', 'post', 'date_posted', 'image', 'author']




class FeedbackSerializer(serializers.ModelSerializer):

  class Meta:
    model = Feedback
    fields = ['id', 'body', 'post', 'author', 'date_posted']