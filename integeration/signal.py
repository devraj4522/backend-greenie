from django.core.signals import Signal
from django.dispatch import receiver
from .tasks import test_task

test_signal = Signal()
email_sent = Signal()

@receiver(email_sent)
def test_signal(sender, **kwargs):
    print(sender)
    test_task.delay()
    print("signal recieved")


@receiver(email_sent)
def send_email_task(sender, **kwargs):
    # print(sender)
    to = kwargs.get('to')
    subject = kwargs.get('subject')
    message = kwargs.get('message')
    # send_email.delay(to, subject, message)
