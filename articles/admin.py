from django.contrib import admin
from .models import ArticlePost, Comment
# Register your models here.
admin.site.register(ArticlePost)
admin.site.register(Comment)