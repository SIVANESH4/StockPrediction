from .models import Student_table
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_table
        fields = '__all__'
