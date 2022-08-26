from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import InfoPaciente,ListaPersonalSalud,InfoPersonalSalud, PacienteViewSet, HistoriaPacienteViewSet, SignosVitalesViewSet

router=DefaultRouter()
router.register
router.register(r'pacientes', PacienteViewSet)
router.register(r'historias_pacientes', HistoriaPacienteViewSet)
router.register(r'signos_vitales', SignosVitalesViewSet)

urlpatterns = [
    path('lista_personal_salud/', ListaPersonalSalud.as_view(), name="lista_personal_salud"),
    path('info_personal_salud/<pk>', InfoPersonalSalud.as_view(), name="info_personal_salud"),
    path('info_paciente/<pk>', InfoPaciente.as_view(), name="info_paciente"),
]

urlpatterns += router.urls