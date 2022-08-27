from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PersonalSaludViewSet,UsuarioPacienteViewSet,UsuarioPsaludViewSet,UsuarioFamiliarViewSet,UserViewSet,FamiliarViewSet,InfoPaciente,ListaPersonalSalud,InfoPersonalSalud, PacienteViewSet, HistoriaPacienteViewSet

router=DefaultRouter()
router.register
router.register(r'usuarios', UserViewSet)
router.register(r'pacientes', PacienteViewSet)
router.register(r'usuario_paciente', UsuarioPacienteViewSet)
router.register(r'historias_pacientes', HistoriaPacienteViewSet)
router.register(r'familiares', FamiliarViewSet)
router.register(r'usuario_familiar', UsuarioFamiliarViewSet)
router.register(r'personal_salud', PersonalSaludViewSet)
router.register(r'usuario_personal_salud',UsuarioPsaludViewSet)

urlpatterns = [
    path('lista_personal_salud/', ListaPersonalSalud.as_view(), name="lista_personal_salud"),
    path('info_personal_salud/<pk>', InfoPersonalSalud.as_view(), name="info_personal_salud"),
    path('info_paciente/<pk>', InfoPaciente.as_view(), name="info_paciente"),
]

urlpatterns += router.urls