from django.urls import path
from .views import company_value

urlpatterns = [
    path('company-value/', company_value, name='company_value'),
]
