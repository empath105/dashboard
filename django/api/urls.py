from django.urls import path
from .views import run_sir_model

urlpatterns = [
    path('api/run_sir/', run_sir_model, name='run_sir'),
]