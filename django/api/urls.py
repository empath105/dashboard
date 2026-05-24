from django.urls import path
from .views import run_sir_model, run_turing_model, run_fkpp_model

urlpatterns = [
    path('api/run_sir/', run_sir_model, name='run_sir'),
    path('api/run_turing/', run_turing_model, name='run_turing'),
    path('api/run_fkpp/', run_fkpp_model, name='run_fkpp'),
]