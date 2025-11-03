from celery import shared_task
from django.core.management import call_command
import time

@shared_task
def celery_test_task():
    time.sleep(10)  # Simulating a time-consuming task
    return 'Task executed successfully'

@shared_task
def import_data_task(file_path, model_name):
    try:
        call_command('importdata', file_path, model_name)
        
    except Exception as e:
        raise e
    
    return 'Data imported successfully.'
