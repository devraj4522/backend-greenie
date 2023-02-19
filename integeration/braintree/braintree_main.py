import braintree
import os
from dotenv import load_dotenv


load_dotenv()

class BrainTreeException(Exception):
    def __init__(self, error_msg):
        self.error_msg = error_msg

    def __str__(self) :
         return self.error_msg

class BrainTreeMain(object):
    def __init__(self, mode="TEST"):
        self.mode = mode
        self.merchant_id = os.getenv("MERCHANT_ID")
        self.public_key=os.getenv("PUBLIC_KEY")
        self.private_key=os.getenv("PRIVATE_KEY")
        self.gateway = self.__create_gateway()

    def __create_gateway(self):
        try:
            gateway = braintree.BraintreeGateway(
                braintree.Configuration(
                    braintree.Environment.Sandbox,
                    merchant_id=self.merchant_id,
                    public_key=self.public_key,
                    private_key=self.private_key
                )
            )
        except Exception as e:
            raise BrainTreeException("Error in creating Braintree Gateway: {e}")
        return gateway


    
    def generate_token(self):
        try:
            token = self.gateway.client_token.generate()
        except Exception as e:
            raise BrainTreeException(f'Error  in generaing braintree payment token: \n {e}')
        return {'clientToken': token, 'success': True}


    def process_payment(self, payment_nonce, amount):
        # if not self.__validate_user_session(id, token):
        #     return {'error': 'Invalid session, Please login again!'}

        # nonce_from_the_client = request.POST["paymentMethodNonce"]
        # amount_from_the_client = request.POST["amount"]
        try:
            result = self.gateway.transaction.sale({
                "amount": amount,
                "payment_method_nonce": payment_nonce,
                "options": {
                    "submit_for_settlement": True
                }
            })

            if result.is_success:
                return {"error": False,  "success": result.is_success, 'transaction': {'id': result.transaction.id, 'amount': result.transaction.amount}}
            else:
                return {'error': True, 'sucess': False}
        except Exception as e:
            raise BrainTreeException(f"Exception in Braintree API:\n {e}")

# if __name__=='__main__':
#     braintree = BrainTreeMain()
#     token = braintree.gateway.client_token.generate()
#     print(token)