from .braintree_main import BrainTreeException, BrainTreeMain
from backend_greenie.users.models import User
from django.core.exceptions import ObjectDoesNotExist


class BrainTreeWrapper(object):
    def __init__(self, mode='TEST'):
        if mode not in ('TEST', 'PROD'):
            raise BrainTreeException('Payment mode must be test or prod')
        self.mode = mode
        self.brain_tree = BrainTreeMain(self.mode)

    def make_payment(self, nonce, amount):
        
        return self.brain_tree.process_payment(payment_nonce=nonce, amount=amount)