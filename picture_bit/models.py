from django.db import models
from PIL import Image
from django.utils import timezone
from review_bit.models import Review

# Create your models here.

class Picture(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    picture_files = models.ImageField(upload_to="review_pics", null=True, blank=True)
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.review.title}'s picture"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.picture_files.path)
        if img.height > 900 or img.width > 1600:
            output_size = (1600, 900)
            img.thumbnail(output_size)
            img.save(self.picture_files.path)
