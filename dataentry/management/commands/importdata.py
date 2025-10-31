from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import csv 

class Command(BaseCommand):
    help = 'Import data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')
        parser.add_argument('model_name', type=str, help='Name of the model')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        model_name = kwargs['model_name'].capitalize()

        # search for the model across all installed apps
        model = None
        for app_config in apps.get_app_configs():
             #Try search for the model in each app
             try:
                  model = apps.get_model(app_config.label, model_name)
                  break # stop searching once the model is found
             except LookupError:
                    continue # model not found in this app, continue searching in next app
             
        if not model:
            raise CommandError(f'Model "{model_name}" not found in any installed app.')   
            

        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                    model.objects.create(**row)
        self.stdout.write(self.style.SUCCESS('Data imported from CSV successfully.'))