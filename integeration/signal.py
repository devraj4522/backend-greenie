from django.core.signals import Signal
from django.dispatch import receiver
from .tasks import test_task, send_mail_task

test_signal = Signal(providing_args=[""])
email_sent = Signal(providing_args=["to_users", "subject", "html_content"])

@receiver(test_signal)
def test_signal_s(sender, **kwargs):
    print("signal started")
    test_task.delay()
    print("signal recieved")

# test_signal.send(sender=None)

@receiver(email_sent)
def send_email_signal(sender, **kwargs):
    # print(sender)
    to_users = kwargs.get('to_users')
    subject = kwargs.get('subject')
    message = kwargs.get('html_content')
    send_mail_task.delay(to_users, subject, message)
