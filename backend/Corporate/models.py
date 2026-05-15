from django.db import models

class Emp_table(models.Model):
    e_id = models.CharField(max_length=20)
    e_name = models.CharField(max_length=100)
    e_desgination = models.CharField(max_length=20)
    e_team = models.CharField(max_length=20)
    e_salary = models.IntegerField(max_length=10)
    e_doj = models.DateField()


