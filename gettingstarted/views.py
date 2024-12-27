from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def products(request):
    data = {
        "company": "Ualá",
        "products": [
            {"productName": "Cuenta Remunerada", "value": "40%"},
            {"productName": "Fondo Común de Inversión", "value": "37.42%"},
            {"productName": "Plazo Fijo", "value": "TNA 30 días: 33% | TNA 90 días: 35% | TNA 180 días: 40% | TNA 365 días: 45%"}
        ]
    }
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})
