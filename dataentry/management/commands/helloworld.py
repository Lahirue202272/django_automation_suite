from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Outputs Hello, World! to the console'

    def handle(self, *args, **kwargs):
        self.stdout.write('Hello, World!')

    