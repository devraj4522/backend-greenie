from .braintree_main import BrainTreeException, BrainTreeMain
from backend_greenie.users.models import User
from django.core.exceptions import ObjectDoesNotExist


class BrainTreeWrapper(object):
    def __init__(self, mode):
        if mode not in ('TEST', 'PROD'):
            raise BrainTreeException('Payment mode must be test or prod')
        self.mode = mode
        self.brain_tree = BrainTreeMain(self.mode)
        self.__validate_user_session()  #if session is not valid raise error
        self.payment_token = self.brain_tree.generate_token()

    def __validate_user_session(self, user_id, token):
        try:
            user = User.objects.get(id=user)
        except ObjectDoesNotExist as e:
            raise BrainTreeException('Invalid session, Please login again!')
        return user.auth_token == token
    def make_payment(self, nonce, amount):
        
        self.brain_tree.process_payment(id='2', token=self.payment_token, payment_nonce=nonce, amount=amount)