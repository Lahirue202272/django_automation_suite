import csv
from django.core.management.base import BaseCommand
from django.apps import apps
import datetime

class Command(BaseCommand):
    help = 'Export data from the database to a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help='Model name')


    def handle(self, *args, **kwargs):
        model_name = kwargs['model_name'].capitalize()

        #search through all installed apps to find the model
        model = None
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label,model_name)
                break
            except LookupError:
                continue

        if not model:
            self.stderr.write(f'Model "{model_name}" not found in any installed app.')
            return
        
        #fetch the data from the database
        data =model.objects.all()

        # generate the timestamp of current date and time
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

        # Define the CSV file path
        file_path = f'exported_{model_name}_data_{timestamp}.csv'

        #open the CSV file and write the data
        with open(file_path,'w',newline='') as file:
            writer = csv.writer(file)
            # Write the CSV header

            #we want to print the fields name of the model that we are trying to export
            writer.writerow([field.name for field in model._meta.fields])

            # Write student data
            for dt in data:
                writer.writerow([getattr(dt, field.name) for field in model._meta.fields])
        
        self.stdout.write(self.style.SUCCESS(f'Data exported successfully to {file_path}'))
            