from django.contrib import admin
from .models import Quiz, QuizResponses

# Register your models here.

admin.site.register(Quiz)
admin.site.register(QuizResponses)