from rest_framework import serializers
from .models import ArticlePost, Comment


class ArticleSerializer(serializers.ModelSerializer):

  class Meta:
    model = ArticlePost
    fields = ['id', 'title', 'post', 'date_posted', 'image', 'author']




class CommentSerializer(serializers.ModelSerializer):

  class Meta:
    model = Comment
    fields = ['id', 'body', 'post', 'author', 'image', 'date_posted']