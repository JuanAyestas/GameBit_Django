from django.db import models
from PIL import Image
from django.utils import timezone
import io
from django.core.files.storage import default_storage as storage
from review_bit.models import Review

# Create your models here.

class Picture(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    picture_files = models.ImageField(upload_to="review_pics", null=True, blank=True)
    uploaded_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ["-uploaded_at",]

    def __str__(self):
        return f"{self.review.title}'s picture, uploaded on: {self.uploaded_at}"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img_read = storage.open(self.picture_files.name, 'rb')
        img = Image.open(img_read)
        
        if img.height > 900 or img.width > 1600:
            output_size = (1600, 900)
            img.thumbnail(output_size)
            in_mem_file = io.BytesIO()
            img.convert('RGB').save(in_mem_file, format='JPEG')
            img_write = storage.open(self.picture_files.name, 'w+')
            img_write.write(in_mem_file.getvalue())
            img_write.close()
        img_read.close()
