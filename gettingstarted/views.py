from django.http import JsonResponse

def company_value(request):
    data = {
        "company": "Ualá",
        "products": [
            {"productName": "Cuenta Remunerada", "value": "45%"},
            {"productName": "Fondo Común de Inversión", "value": "35.04%"},
            {"productName": "Plazo Fijo", "value": "TNA 30 días: 37% | TNA 90 días: 40% | TNA 180 días: 45% | TEA 30 días: 43.98% | TEA 90 días: 46.45% | TEA 180 días: 50.14%"}
        ]
    }
    return JsonResponse(data)

