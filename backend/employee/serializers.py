from .models import Employee_table
from rest_framework import serializers

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_table
        fields = '__all__'
