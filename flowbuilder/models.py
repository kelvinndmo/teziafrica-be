from django.db import models
from authentication.models import Company


class ChatInput(models.Model):
  company = models.ForeignKey(Company, on_delete=models.CASCADE)
  title = models.CharField(max_length=255)

  def __str__(self):
      return f'Chat Content: {self.title} | Company: {self.company}'

    

class ChatOutPut(models.Model):
  chatinput = models.ForeignKey(ChatInput, null=True, default=None, on_delete=models.CASCADE)
  reply = models.CharField(max_length=255, default=None)
  author = models.ForeignKey(Company, on_delete = models.CASCADE)
  order = models.IntegerField()

  class Meta:
    unique_together=('chatinput', 'order')

  def __str__(self):
      return f'Chat OutPut: {self.reply} | Company: {self.author}'