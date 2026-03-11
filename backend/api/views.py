from django.http import JsonResponse

# Create your views here.
def stdapi(request):
    students = [
        {
         'id':1,
         'Name': 'Siva',
         'Dept': 'IT',
        },
    ]
    return JsonResponse(students, safe=False)