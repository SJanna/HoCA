from .models import PersonalSalud,Paciente,HistoriaPaciente,SignosVitales
from .serializers import PersonalSaludSerilizer,PacienteSerilizer,HistoriaPacienteSerilizer,SignosVitalesSerilizer 
from django.contrib.auth.models import User
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from .permissions import IsMedicoOwner
from rest_framework import viewsets
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
class ListaPersonalSalud(APIView):
    """Solo Administradores tienen acceso a esta vista"""
    permission_classes = [permissions.IsAdminUser]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'hospital/lista_personal_salud.html'

    def get(self, request):
        queryset = PersonalSalud.objects.all()
        return Response({'personal_salud': queryset})

class InfoPersonalSalud(APIView):
    """Solo el personal de salud proprietario tienen acceso a esta vista"""
    permission_classes=[IsMedicoOwner, permissions.IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'hospital/info_personal_salud.html'

    def get(self, request, pk):
        personal_salud = get_object_or_404(PersonalSalud, pk=pk)
        pacientes = Paciente.objects.filter(personal_salud=personal_salud)
        serializer = PersonalSaludSerilizer(personal_salud)
        self.check_object_permissions(self.request, personal_salud)
        return Response({'serializer': serializer, 'personal_salud': personal_salud, 'pacientes': pacientes})

    def post(self, request, pk):
        personal_salud = get_object_or_404(PersonalSalud, pk=pk)
        serializer = PersonalSaludSerilizer(personal_salud, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'personal_salud': personal_salud})
        serializer.save()
        return render(request, 'site/name.html', {})

class InfoPaciente(APIView):
    """Solo el PersonalSalud proprietario tienen acceso a esta vista"""
    permission_classes=[permissions.IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'hospital/info_paciente.html'

    def get(self, request, pk):
        paciente = get_object_or_404(Paciente, pk=pk)
        serializer = PacienteSerilizer(paciente)
        self.check_object_permissions(self.request, paciente)
        return Response({'serializer': serializer, 'paciente': paciente})

    def post(self, request, pk):
        personal_salud = get_object_or_404(PersonalSalud, pk=pk)
        serializer = PersonalSaludSerilizer(personal_salud, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'personal_salud': personal_salud})
        serializer.save()
        return redirect('lista_medicos')

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