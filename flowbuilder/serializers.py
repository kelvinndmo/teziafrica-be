from rest_framework import serializers
from .models import ChatInput, ChatOutPut


class ChatInputSerializer(serializers.ModelSerializer):

  class Meta:
    model = ChatInput
    fields = ['id', 'company', 'title']



class ChatOutPutSerializer(serializers.ModelSerializer):

  class Meta:
    model = ChatOutPut
    fields = ['id', 'chatinput', 'reply', 'author', 'order']