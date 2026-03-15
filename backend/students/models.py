from django.db import models

# Create your models here.
class Student_table(models.Model):
    name = models.CharField(max_length=50)
    rollno = models.CharField(max_length=30)
    dept = models.CharField(max_length=20)

    def __str__(self):
        return self.name