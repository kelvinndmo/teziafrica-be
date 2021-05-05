from django.db import models
from authentication.models import User


class Quiz(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=255)

  def __str__(self):
    return '%s - %s' % (self.title, self.user)

    

class QuizResponses(models.Model):
  quiz = models.ForeignKey(Quiz, null=True, default=None, on_delete=models.CASCADE)
  reply = models.CharField(max_length=255, default=None)
  author = models.ForeignKey(User, on_delete = models.CASCADE)
  order = models.IntegerField()

  class Meta:
    unique_together=('quiz', 'order')

  def __str__(self):
    return '%s - %s' % (self.reply, self.author)
