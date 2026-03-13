from django.http import JsonResponse
from students.models import Student

# Create your views here.
def stdapi(request):
    std = Student.objects.all()
    std_list = list(std.values())
    return JsonResponse(std_list, safe=False)