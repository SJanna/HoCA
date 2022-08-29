from .models import Familiar, PersonalSalud,Paciente,HistoriaPaciente, SignosVitales
from .serializers import PersonalSaludSerilizer,PacienteSerilizer,HistoriaPacienteSerilizer,SignosVitalesSerilizer,FamiliarSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner, IsAuxiliar, IsPaciente, IsPersonalSalud, VeSignosVitales, IsHistoriaPaciente
from rest_framework import viewsets
from rest_framework import generics
import django_filters.rest_framework
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import filters
from hospital import serializers
from rest_framework import status
from django.http import Http404
from rest_framework import generics

def Inicio(request):
    return render(request, "hospital/inicio.html")

# ApiViews

class PerfilPaciente(APIView):
    """Solo Administradores tienen acceso a esta vista"""
    permission_classes = [IsPaciente]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'hospital/perfil_paciente.html'

    def get(self, request):
        paciente = get_object_or_404(Paciente, usuario=request.user.id)
        signos_vitales = SignosVitales.objects.filter(paciente=paciente).all()
        self.check_object_permissions(self.request, paciente)
        return Response({'paciente': paciente, 'signos_vitales': signos_vitales})

class PerfilPersonalSalud(APIView):
    """Solo el personal de salud proprietario tienen acceso a esta vista"""
    permission_classes=[IsPersonalSalud]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'hospital/perfil_personal_salud.html'

    def get(self, request):
        personal_salud = get_object_or_404(PersonalSalud, usuario=request.user.id) #Datos del Usuario(Modelo PersonalSalud)
        pacientes = Paciente.objects.filter(personal_salud=personal_salud) #Pacientes asociados al personal_salid
        self.check_object_permissions(self.request, personal_salud)
        return Response({'personal_salud': personal_salud, 'pacientes': pacientes})


#ViewSets
class HistoriaPacienteViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = HistoriaPaciente.objects.all()
    serializer_class = HistoriaPacienteSerilizer
    permission_classes = [permissions.IsAdminUser | IsPersonalSalud | IsHistoriaPaciente]
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    ordering_fields = '__all__'

    def get_queryset(self, *args, **kwargs):
        try:
            usuario=self.request.user
            paciente=Paciente.objects.get(usuario=usuario)
            paciente=paciente.id
            return HistoriaPaciente.objects.all().filter(paciente=paciente)
        except:
           return  HistoriaPaciente.objects.all()
            # usuario=self.request.user
            # doctor=PersonalSalud.objects.get(usuario=usuario)
            # doctor=doctor.id
            # return  HistoriaPaciente.objects.all().filter(doctor=doctor)

class PacienteViewSet(viewsets.ModelViewSet):
    """
    Permite  `crear`, `borrar`, `actualizar` y `visualizar` la información de los pacientes
    """
    permission_classes = [IsAuxiliar | permissions.IsAdminUser]
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerilizer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['nombre', 'apellidos','numero_id']
    ordering_fields = '__all__'

class PersonalSaludViewSet(viewsets.ModelViewSet):
    
    permission_classes = [IsAuxiliar | permissions.IsAdminUser]
    queryset = PersonalSalud.objects.all()
    serializer_class = PersonalSaludSerilizer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['nombre', 'apellidos','numero_id']
    ordering_fields = '__all__'
    
class FamiliarViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuxiliar | permissions.IsAdminUser]    
    queryset = Familiar.objects.all()
    serializer_class = FamiliarSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['nombre', 'apellidos','numero_id']
    ordering_fields = '__all__'

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuxiliar | permissions.IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['username', 'email']
    ordering_fields = '__all__'

class PersonalSaludViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuxiliar | permissions.IsAdminUser]
    queryset = PersonalSalud.objects.all()
    serializer_class = PersonalSaludSerilizer
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['nombre', 'apellidos','numero_id']
    ordering_fields = '__all__'

class SignosVitalesApi(viewsets.ModelViewSet):
    
    queryset = SignosVitales.objects.all()
    serializer_class = SignosVitalesSerilizer
    permission_classes = [permissions.IsAdminUser | IsPaciente]
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['id','created_at', 'updated_at']
    ordering_fields = '__all__'

    def get_queryset(self, *args, **kwargs):
        usuario=self.request.user
        paciente=Paciente.objects.get(usuario=usuario)
        paciente=paciente.id
        return SignosVitales.objects.all().filter(paciente=paciente)
