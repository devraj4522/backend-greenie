from django.db import models
from django_extensions.db.models import TimeStampedModel
from backend_greenie.users.models import User
from user.models import GreenieUser, DeleveryAddress
from django.core.validators import MaxValueValidator, MinValueValidator
from shortuuid.django_fields import ShortUUIDField
from product.models import Product, Category
from .model_helpers import TxnType, StatusType


class Purchase(TimeStampedModel):
    id = ShortUUIDField(length=8, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ", primary_key=True, editable=False)
    address = models.ForeignKey(DeleveryAddress, on_delete=models.CASCADE, null=True, blank=True, related_name='purchases')


class Order(TimeStampedModel):
    id = ShortUUIDField(length=8, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ", primary_key=True, editable=False)
    user = models.ForeignKey(GreenieUser, on_delete=models.CASCADE, related_name='orders')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')
    status = models.CharField(max_length=30, default=StatusType.ADDED_TO_CART, choices=StatusType.choices)
    is_active = models.BooleanField(default=True)

class Txn(TimeStampedModel):
    id = ShortUUIDField(length=8, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ", primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='txns')
    type = models.CharField(max_length=15, default=TxnType.DEBIT, choices=TxnType.choices)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='txns')
    amt = models.IntegerField(default=0)
    txn_date = models.DateField(blank=True, null=True)
    note =  models.TextField(blank=True, null=True)
    type = models.CharField(max_length=15, default=TxnType.DEBIT, choices=TxnType.choices)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True, related_name='txns')
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, null=True, blank=True, related_name='txns')