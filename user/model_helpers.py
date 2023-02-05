from django.db import models

class GenderType(models.TextChoices):
    MALE = 'MALE','MALE'
    FEMALE = 'FEMALE','FEMALE'
    OTHER = 'OTHER','OTHER'

class AddressType(models.TextChoices):
    HOME = 'HOME', 'HOME'
    WORK = 'WORK', 'WORK'
    