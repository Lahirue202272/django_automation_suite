from awd_main.celery import app
from dataentry.utils import send_email_notification
from celery import shared_task

@shared_task
def send_email_task(mail_subject,body,to_email,attachment):
    send_email_notification(mail_subject,body,to_email,attachment)
    return 'Email sending task successfully'
