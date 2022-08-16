from django.http import JsonResponse

# Create your views here.


def home(request):
    return JsonResponse({'info': 'Django ReactAPI', 'name': "Dev Raj Singh"})
