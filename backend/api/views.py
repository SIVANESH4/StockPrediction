from students.models import Student
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StudentSerializers

# Create your views here.
@api_view(['GET'])
def stdapi(request):
    if request.method == 'GET':
        student_details = Student.objects.all()
        serialized_data = StudentSerializers(student_details, many = True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    return HttpResponse('<p> Failed </p>')

    