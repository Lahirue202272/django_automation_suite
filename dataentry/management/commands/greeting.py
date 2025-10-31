from django.core.management.base import BaseCommand


# Proposed command = python manage.py greeting lahiru

class Command(BaseCommand):
    help='Outputs a greeting message to the console'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Name to greet')

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        greeting = f'Hi {name} Good Morning!'
        self.stdout.write(greeting)