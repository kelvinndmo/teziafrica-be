from django.db import models
from authentication.models import Company
from utils.models import BaseAbstractModel
from cloudinary.models import CloudinaryField
from cloudinary import CloudinaryImage
from django.dispatch import receiver
from django.core.files import File
from PIL import Image


class ChatInput(models.Model):
  company = models.ForeignKey(Company, on_delete=models.CASCADE)
  image = models.ImageField('Image file', upload_to='tezi_images/chatinput', null=True)
  title = models.CharField(max_length=255)

  def __str__(self):
      return f'Chat Content: {self.title} | Company: {self.company}'
  
  def delete(self, *args, **kwargs):
	   storage, path = self.image.storage, self.image.name
	   super().delete(*args, **kwargs)
	   storage.delete(path)

    

class ChatOutPut(models.Model):
  chatinput = models.ForeignKey(ChatInput, null=True, default=None, on_delete=models.CASCADE)
  image = models.ImageField('Image file', upload_to='tezi_images/chatoutput', null=True)
  reply = models.CharField(max_length=255, default=None)
  author = models.ForeignKey(Company, on_delete = models.CASCADE)
  order = models.IntegerField()

  class Meta:
    unique_together=('chatinput', 'order')

  def __str__(self):
      return f'Chat OutPut: {self.reply} | Company: {self.author}'
  
  def delete(self, *args, **kwargs):
	    storage, path = self.image.storage, self.image.name
	    super().delete(*args, **kwargs)
	    storage.delete(path)