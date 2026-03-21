from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import EmployeeSerializer
from .models import Employee_table
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.
class Employees(APIView):
    def get(self, request):
        employee = Employee_table.objects.all()
        serializer = EmployeeSerializer(employee, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class EmployeesDetails(APIView):
    def get_object(self, pk):
        try:
            return Employee_table.objects.get(pk = pk) 
        except Employee_table.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        emp = self.get_object(pk)
        serializer = EmployeeSerializer(emp)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        emp = self.get_object(pk)
        serializer = EmployeeSerializer(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        emp = self.get_object(pk)
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
