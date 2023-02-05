from django.db import models
from django_extensions.db.models import TimeStampedModel
from shortuuid.django_fields import ShortUUIDField
from backend_greenie.users.models import User
from .model_helpers import GenderType, AddressType

class GreenieUser(TimeStampedModel):
    id = ShortUUIDField(length=8, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ", primary_key=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='greenie_user')
    name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    active = models.BooleanField(default=True)
    email = models.EmailField(blank=True, null=True)
    images = models.JSONField(default=dict)
    gender = models.CharField(max_length=15, default=GenderType.MALE, choices=GenderType.choices)

    class Meta:
        db_table = 'greenie_user'

    def __str__(self):
        return self.user.username if self.user.username else self.id

    def can_login(self):
        can_login = {}

        if self.active:
            return {
                "active_user" : True,
                "error_msg" :  None
            }
        else :
            return {
                "active_user" : False,
                "error_msg" :  "User is set to inactive, please contact site admin"
            }


class DeleveryAddress(TimeStampedModel):
    id = ShortUUIDField(length=8, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ", primary_key=True, editable=False)
    user = models.ForeignKey(GreenieUser, on_delete=models.CASCADE, related_name='addresses')
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    address = models.CharField(max_length=400)
    pincode = models.CharField(max_length=6)
    phone = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    type = models.CharField(max_length=15, default=AddressType.HOME, choices=AddressType.choices)

    class Meta:
        db_table = 'delevery_address'


class Contact(TimeStampedModel):
    id = ShortUUIDField(length=8, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ", primary_key=True, editable=False)
    title = models.CharField(max_length=50, default='Anonymous')
    msg = models.CharField(max_length=500, blank=True, null=True)
    user = models.ForeignKey(
        GreenieUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title