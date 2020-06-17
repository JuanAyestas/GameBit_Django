from django.db import models
from django.utils import timezone
from django.urls import reverse
from PIL import Image
from django.contrib.auth.models import User

# Create your models here.

class Meme(models.Model):
  caption = models.CharField(max_length=120)
  meme = models.ImageField(upload_to="memes")
  date_posted = models.DateTimeField(default=timezone.now)
  #relationship with User
  author = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"Meme: {self.caption}, {self.date_posted}"
  
  def get_absolute_url(self):
      return reverse("gamebit-meme-full", kwargs={"pk": self.pk})

  def save(self, *args, **kwargs):
      super().save(*args, **kwargs)
      img = Image.open(self.meme.path)
      if img.height > 900 or img.width > 1600:
          output_size = (1600, 900)
          img.thumbnail(output_size)
          img.save(self.meme.path)
