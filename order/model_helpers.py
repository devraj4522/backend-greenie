from django.db import models

class TxnType(models.TextChoices):
    CREDIT = 'CREDIT','CREDIT'  # Credit to user for refund
    DEBIT = 'DEBIT','DEBIT'     # Debit by user

class StatusType(models.TextChoices):
    VIEWED = 'VIEWED', 'VIEWED'
    ADDED_TO_CART = 'ADDED_TO_CART','ADDED_TO_CART'  
    PAYMENT_PENDING = 'PAYMENT_PENDING','PAYMENT_PENDING'
    PAYMENT_DONE = 'PAYMENT_DONE','PAYMENT_DONE'
    RETURNED = 'RETURNED', 'RETURNED'
    REFUNDED = 'REFUNDED', 'REFUNDED'
    REFUNDED_DESPUTED = 'REFUNDED_DESPUTED', 'REFUNDED_DESPUTED'
