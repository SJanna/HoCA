from unicodedata import name
from rest_framework.routers import DefaultRouter
from .views import SignosVitalesApi, PersonalSaludViewSet,UserViewSet,FamiliarViewSet, PacienteViewSet, HistoriaPacienteViewSet

router=DefaultRouter()
router.register(r'usuarios', UserViewSet, basename="usuarios")
router.register(r'pacientes', PacienteViewSet)
router.register(r'historias_pacientes', HistoriaPacienteViewSet, basename="historias")
router.register(r'familiares', FamiliarViewSet)
router.register(r'personal_salud', PersonalSaludViewSet)
router.register(r'signos_vitales', SignosVitalesApi, basename="signos_vitales")

urlpatterns = router.urls