from django.urls import path, include
from .views import PerfilPaciente,PerfilPersonalSalud, Inicio

urlpatterns = [
    path('perfil_paciente/', PerfilPaciente.as_view(), name="perfil_paciente"),
    path('perfil_personal_salud/', PerfilPersonalSalud.as_view(), name="perfil_personal_salud"),
    path('api/', include('hospital.routers')),
    path('', Inicio, name="inicio"),
    path('', include('rest_framework.urls', namespace='rest_framework')),
]