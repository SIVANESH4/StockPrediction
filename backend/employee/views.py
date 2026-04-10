from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from .serializers import EmployeeSerializer
from .models import Employee_table
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import mixins, generics, viewsets

# Create your views here.
'''
class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Employee_table.objects.all()
    serializer_class = EmployeeSerializer
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class EmployeesDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Employee_table.objects.all()
    serializer_class = EmployeeSerializer
    def get(self, request, pk):
        return self.retrieve(request, pk)
    def put(self, request, pk):
        return self.update(request, pk)
    def delete(self, request, pk):
        return self.destroy(request, pk)
'''

'''
class Employees(generics.ListCreateAPIView):
    queryset = Employee_table.objects.all()
    serializer_class = EmployeeSerializer

class EmployeesDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee_table.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'
'''

'''class EmployeeViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Employee_table.objects.all()
        serializer = EmployeeSerializer(queryset, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def retrieve(self, request, pk=None):
        employee = get_object_or_404(Employee_table,pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)'''
        

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee_table.objects.all()
    serializer_class = EmployeeSerializer