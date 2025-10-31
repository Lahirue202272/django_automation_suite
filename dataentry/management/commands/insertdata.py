from django.core.management.base import BaseCommand
from dataentry.models import Student

class Command(BaseCommand):
    help = 'Inserts sample data into the database'

    def handle(self, *args, **kwargs):
        dataset =[
            {'roll_no': 1002, 'name': 'Lahiru', 'age': 21},
            {'roll_no': 1003, 'name': 'Bob', 'age': 22},
            {'roll_no': 1004, 'name': 'Charlie', 'age': 23},
            {'roll_no': 1005, 'name': 'David', 'age': 24},
            {'roll_no': 1006, 'name': 'Eve', 'age': 25},
        ]

        for data in dataset:
            roll_no = data['roll_no']
            existing_record = Student.objects.filter(roll_no=roll_no).exists()
            if not existing_record:
                Student.objects.create(roll_no=data['roll_no'], name=data['name'], age=data['age'])
            else:
                self.stdout.write(self.style.WARNING(f'Student with roll_no {roll_no} already exists.'))

        self.stdout.write(self.style.SUCCESS('Sample data inserted successfully.'))