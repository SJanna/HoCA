from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import SignosVitalesApi,AñadirSignosVitales,PerfilPaciente, PersonalSaludViewSet,UserViewSet,FamiliarViewSet,PerfilPersonalSalud, PacienteViewSet, HistoriaPacienteViewSet

router=DefaultRouter()
router.register
router.register(r'usuarios', UserViewSet)
router.register(r'pacientes', PacienteViewSet)
router.register(r'historias_pacientes', HistoriaPacienteViewSet)
router.register(r'familiares', FamiliarViewSet)
router.register(r'personal_salud', PersonalSaludViewSet)

urlpatterns = [
    path('perfil_paciente/<pk>', PerfilPaciente.as_view(), name="perfil_paciente"),
    path('perfil_personal_salud/<pk>', PerfilPersonalSalud.as_view(), name="perfil_personal_salud"),
    path('signos_vitales/<pk>', SignosVitalesApi.as_view(), name="signos_vitales"),
    path('añadir_sv/', AñadirSignosVitales.as_view(), name="añadir_sv"),

]

urlpatterns += router.urls