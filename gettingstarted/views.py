from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def products(request):
    data = {
        "company": "Ualá",
        "products": [
            {"productName": "Cuenta Remunerada", "value": "45%"},
            {"productName": "Fondo Común de Inversión", "value": "35.04%"},
            {"productName": "Plazo Fijo", "value": "TNA 30 días: 38% | TNA 90 días: 40% | TNA 180 días: 45% | TEA 30 días: 43.98% | TEA 90 días: 46.45% | TEA 180 días: 45% | TEA 365 días: 50%"}
        ]
    }
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})
