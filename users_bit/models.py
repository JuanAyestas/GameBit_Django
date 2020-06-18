from django.db import models
from django.utils import timezone
from PIL import Image
from django.contrib.auth.models import User
import io
from django.core.files.storage import default_storage as storage

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default="default.jpg", upload_to="profile_pics")
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username}'s Profile on {self.date_created}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img_read = storage.open(self.image.name, 'rb')
        img = Image.open(img_read)
        
        if img.height > 225 or img.width > 400:
            output_size = (400, 225)
            img.thumbnail(output_size)
            in_mem_file = io.BytesIO()
            img.convert('RGB').save(in_mem_file, format='JPEG')
            img_write = storage.open(self.image.name, 'w+')
            img_write.write(in_mem_file.getvalue())
            img_write.close()
        img_read.close()
