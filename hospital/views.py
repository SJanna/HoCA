from .models import Medico,Paciente,HistoriaPaciente,SignosVitales
from .serializers import MedicoSerilizer,PacienteSerilizer,HistoriaPacienteSerilizer,SignosVitalesSerilizer 
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import viewsets
# Create your views here.
class MedicoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Medico.objects.all()
    serializer_class = MedicoSerilizer

class PacienteViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerilizer

class HistoriaPacienteViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = HistoriaPaciente.objects.all()
    serializer_class = HistoriaPacienteSerilizer

class SignosVitalesViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = SignosVitales.objects.all()
    serializer_class = SignosVitalesSerilizer