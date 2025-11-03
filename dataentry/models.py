from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    
class Customer(models.Model):
    customer_name = models.CharField(max_length=50)
    country = models.CharField(max_length=10)

    def __str__(self):
        return self.customer_name

class Employee(models.Model):
    employee_id = models.IntegerField()
    employee_name = models.CharField(max_length=25)
    designation = models.CharField(max_length=25)
    salary = models.DecimalField(decimal_places=2, max_digits=10)
    retirement = models.DecimalField(decimal_places=2, max_digits=10)
    other_benefits = models.DecimalField(decimal_places=2, max_digits=10)
    total_benefits = models.DecimalField(decimal_places=2, max_digits=10)
    total_compensation = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.employee_name+'-'+self.designation