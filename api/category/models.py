from asyncio.windows_events import NULL
from email.policy import default
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=50, default="subtitle")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='categories/', blank=True, null=True, default=None)
    
    
    def __str__(self):
        return self.name
