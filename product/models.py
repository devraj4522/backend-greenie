from django.db import models
from django_extensions.db.models import TimeStampedModel
from backend_greenie.users.models import User
from user.models import GreenieUser
from django.core.validators import MaxValueValidator, MinValueValidator
from shortuuid.django_fields import ShortUUIDField
# Create your models here.

class Category(TimeStampedModel):
    id = ShortUUIDField(length=8, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ", primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=50, default="subtitle")
    images = models.JSONField(default=dict)
    active = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'category'
    
    def __str__(self):
        return self.name


class Product(TimeStampedModel):
    id = ShortUUIDField(length=8, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ", primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    price = models.PositiveIntegerField(default=0)
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    images = models.JSONField(default=dict)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name
    

class Review(TimeStampedModel):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    rating = models.IntegerField(default=1, validators=[
                                 MaxValueValidator(5), MinValueValidator(1)])
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE)
    user = models.ForeignKey(
        GreenieUser, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'review'
        
    def __str__(self):
        return self.title
