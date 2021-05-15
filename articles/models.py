from django.db import models
from cloudinary.models import CloudinaryField
from cloudinary import CloudinaryImage
from django.dispatch import receiver
from django.core.files import File
from django.utils import timezone
from tinymce.models import HTMLField
from PIL import Image
from authentication.models import User, Company
# Create your models here.

class ArticlePost(models.Model):
   title = models.CharField(max_length=255)
   post = HTMLField()
   date_posted = models.DateTimeField(default=timezone.now)
   image = models.ImageField('Image file', upload_to='tezi_images/articles', null=True)
   author = models.ForeignKey(Company, on_delete=models.CASCADE)

   def __str__(self):
      return f'Post Title: {self.title} | Company: {self.author}'

   def delete(self, *args, **kwargs):
	   storage, path = self.image.storage, self.image.name
	   super().delete(*args, **kwargs)
	   storage.delete(path)
      
   class Meta:
	   verbose_name_plural = 'Knowledge Hub'



class Comment(models.Model):
   body = models.TextField()
   post = models.ForeignKey(ArticlePost, related_name="comments", on_delete=models.CASCADE)
   image = models.ImageField('Image file', upload_to='tezi_images/comments', null=True)
   author = models.ForeignKey(User, on_delete = models.CASCADE)
   date_posted = models.DateTimeField(default=timezone.now)

   def __str__(self):
      return f'Comment: {self.body} | Post: {self.post}'
   
   def delete(self, *args, **kwargs):
	   storage, path = self.image.storage, self.image.name
	   super().delete(*args, **kwargs)
	   storage.delete(path)
