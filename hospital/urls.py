from rest_framework.routers import DefaultRouter
from .views import MedicoViewSet, PacienteViewSet, HistoriaPacienteViewSet, SignosVitalesViewSet

router=DefaultRouter()
router.register(r'medicos', MedicoViewSet)
router.register(r'pacientes', PacienteViewSet)
router.register(r'historias_pacientes', HistoriaPacienteViewSet)
router.register(r'signos_vitales', SignosVitalesViewSet)
urlpatterns = router.urls