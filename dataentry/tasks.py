from celery import shared_task
from django.core.management import call_command
from django.core.mail import EmailMessage
from django.conf import settings
import time
from .utils import send_email_notification

@shared_task
def celery_test_task():
    time.sleep(10)  # Simulating a time-consuming task
    #send an email notification
    mail_subject = 'Test subject'
    message = 'This is a test email'
    to_email = settings.DEFAULT_TO_EMAIL
    # from_email = settings.DEFAULT_FROM_EMAIL
    # mail = EmailMessage(mail_subject, message, from_email, to=[to_email])
    # mail.send()
    send_email_notification(mail_subject, message, to_email)
    return 'Email sent successfully'

@shared_task
def import_data_task(file_path, model_name):
    try:
        call_command('importdata', file_path, model_name)
        
    except Exception as e:
        raise e
    
    # notify the user by email
    mail_subject = 'Data Import Completed'
    message =' Your data import task has been successful.'
    to_email = settings.DEFAULT_TO_EMAIL
    send_email_notification(mail_subject, message, to_email)
    return 'Data imported successfully.'
