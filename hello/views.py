
from django.http import JsonResponse

def company_value(request):
    data = {
        "company": "Uala",
        "value": "45%"
    }
    return JsonResponse(data)
