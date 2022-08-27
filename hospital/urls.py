from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import PersonalSaludViewSet,UserViewSet,FamiliarViewSet,InfoPaciente,ListaPersonalSalud,InfoPersonalSalud, PacienteViewSet, HistoriaPacienteViewSet

router=DefaultRouter()
router.register
router.register(r'usuarios', UserViewSet)
router.register(r'pacientes', PacienteViewSet)
router.register(r'historias_pacientes', HistoriaPacienteViewSet)
router.register(r'familiares', FamiliarViewSet)
router.register(r'personal_salud', PersonalSaludViewSet)

urlpatterns = [
    path('lista_personal_salud/', ListaPersonalSalud.as_view(), name="lista_personal_salud"),
    path('info_personal_salud/<pk>', InfoPersonalSalud.as_view(), name="info_personal_salud"),
    path('info_paciente/<pk>', InfoPaciente.as_view(), name="info_paciente"),
]

urlpatterns += router.urls