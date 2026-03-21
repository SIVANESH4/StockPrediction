from django.db import models

# Create your models here.
class Employee_table(models.Model):
    emp_id = models.CharField(max_length=20)
    emp_name = models.CharField(max_length=50)
    emp_designation = models.CharField(max_length=20)

    def __str__(self):
        return self.emp_name