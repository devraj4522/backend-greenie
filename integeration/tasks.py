from config import celery_app
from integeration.send_grid.sendgrid_mail import SendInBlueMain
from time import sleep

@celery_app.task()
def test_task():
    print("task started")
    sleep(2)
    print("task completed.")

@celery_app.task(serializer='json')
def send_mail_task(to_users, subject, html_content):
    send_blue = SendInBlueMain()
    send_blue.send_mail(to_users, subject, html_content)
    print("Task Scheduled for mail")