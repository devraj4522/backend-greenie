from turtle import title
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


# class CustomUser(AbstractUser):
#     name = models.CharField(max_length=50, default='Anonymous')
#     email = models.EmailField(max_length=254, unique=True)
#     username = None
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#     phone = models.CharField(max_length=20, blank=True, null=True)
#     gender = models.CharField(max_length=10, blank=True, null=True)
#     session_token = models.CharField(max_length=10, default=0)
#     image = models.ImageField(upload_to='profiles/', blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# class Contact(models.Model):
#     title = models.CharField(max_length=50, default='Anonymous')
#     msg = models.CharField(max_length=500, blank=True, null=True)
#     user = models.ForeignKey(
#         CustomUser, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title
