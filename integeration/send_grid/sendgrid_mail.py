from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()
configuration = sib_api_v3_sdk.Configuration()

class SendInBlueException():
    def __init__(self, error_msg):
        self.error_msg = error_msg
    
    def __str__(self) -> str:
        return self.error_msg

class SendInBlueMain():
    def __init__(self):
        self.api_key = os.environ.get("SEND_IN_BLUE_API_KEY")
        sender_name = os.environ.get("SENDER_NAME")
        sender_email = os.environ.get("SENDER_EMAIL")
        cc_name = os.environ.get("CC_NAME")
        cc_email = os.environ.get("CC_EMAIL")
        bcc_name = os.environ.get("BCC_NAME")
        bcc_email = os.environ.get("BCC_EMAIL")
        reply_to_name = os.environ.get("REPLY_TO_NAME")
        reply_to_email = os.environ.get("REPLY_TO_EMAIL")

        # sender cc, bcc, reply_to setup
        self.sender = (sender_name, sender_email)
        self.cc = (cc_name, cc_email)
        self.bcc = (bcc_name, bcc_email)
        self.repy_to = (reply_to_name, reply_to_email)

    def send_mail(self, to_users: list, subject: str, html_content:str, from_email = None) -> None:
        if from_email:
            self.from_email = from_email

        configuration.api_key['api-key'] = self.api_key
        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
        sender = {"name":self.sender[0],"email":self.sender[1]}
        to = []
        for user in to_users:
            to.append({"name":user[0],"email":user[1]})
        cc = [{"name":self.cc[0], "email": self.cc[1]}]
        bcc = [{"name": self.bcc[0],"email":self.bcc[1]}]
        reply_to = {"name":self.repy_to[0], "email":self.repy_to[1]}
        headers = {"Some-Custom-Name":"unique-id-1234"}
        params = {"parameter":"My param value","subject":"New Subject"}
        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, bcc=bcc, cc=cc, reply_to=reply_to, headers=headers, html_content=html_content, sender=sender, subject=subject)
        
        try:
            api_response = api_instance.send_transac_email(send_smtp_email)
            pprint(api_response)
        except ApiException as e:
            return SendInBlueException("Exception when calling SMTPApi->send_transac_email: %s\n" % e)


if __name__ == "__main__" :
    print("main:")
    # s = SendInBlueMain()
    # s.send_mail([("Dev Raj Singh", "rehansingh.4522@gmail.com")], "Hi", "<h1>close</h1>", ("dev raj singh", "rehansingh.4522@gmail.com"))