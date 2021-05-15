from django.db import models

# Create your models here.
from django.db import models
from cloudinary.models import CloudinaryField
from cloudinary import CloudinaryImage
from django.dispatch import receiver
from django.core.files import File
from django.utils import timezone
from tinymce.models import HTMLField
from PIL import Image
from authentication.models import User, Staff
# Create your models here.

class Ticket(models.Model):
   title = models.CharField(max_length=255)
   post = HTMLField()
   date_posted = models.DateTimeField(default=timezone.now)
   author = models.ForeignKey(User, on_delete=models.CASCADE)

   def __str__(self):
      return f'Ticket: {self.title} | Author: {self.author}'

   def delete(self, *args, **kwargs):
	   storage, path = self.screenshot.storage, self.screenshot.name
	   super().delete(*args, **kwargs)
	   storage.delete(path)
      
   class Meta:
	   verbose_name_plural = 'Tickets'



class Feedback(models.Model):
   body = models.TextField()
   post = models.ForeignKey(Ticket, related_name="feedback", on_delete=models.CASCADE)
   screenshot = models.ImageField('Image file', upload_to='tezi_images/ticketsfeedback', null=True)
   author = models.ForeignKey(Staff, on_delete = models.CASCADE)
   date_posted = models.DateTimeField(default=timezone.now)

   def __str__(self):
      return f'Ticket Feedback: {self.body} | Staff: {self.author}'
   
   def delete(self, *args, **kwargs):
	   storage, path = self.screenshot.storage, self.screenshot.name
	   super().delete(*args, **kwargs)
	   storage.delete(path)
