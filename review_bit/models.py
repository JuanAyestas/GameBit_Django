from django.db import models
from django.utils import timezone
from PIL import Image
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Review(models.Model):
  title = models.CharField(max_length=120, unique=True)
  platform = models.CharField(max_length=120)
  summary = models.TextField()
  content = models.TextField()
  thumbnail = models.ImageField(default="default.jpg", upload_to="thumbnail_pics")
  date_posted = models.DateTimeField(default=timezone.now)
  #relationship with User
  author = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"Review: {self.title}, {self.date_posted}"

  def get_absolute_url(self):
      return reverse("gamebit-detail", kwargs={"pk": self.pk})

  def save(self, *args, **kwargs):
      super().save(*args, **kwargs)
      img = Image.open(self.thumbnail.path)
      if img.height > 900 or img.width > 1600:
          output_size = (1600, 900)
          img.thumbnail(output_size)
          img.save(self.thumbnail.path)
