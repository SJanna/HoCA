from .models import Familiar, PersonalSalud,Paciente,HistoriaPaciente, SignosVitales
from .serializers import PersonalSaludSerilizer,PacienteSerilizer,HistoriaPacienteSerilizer,SignosVitalesSerilizer,FamiliarSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner, IsAuxiliar, IsPersonalSalud
from rest_framework import viewsets
from rest_framework import generics
import django_filters.rest_framework
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import filters
from hospital import serializers

# ApiViews
class PerfilPaciente(APIView):
    """Solo Administradores tienen acceso a esta vista"""
    #permission_classes = [IsOwner]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'hospital/perfil_paciente.html'

    def get(self, request, pk):
        paciente = get_object_or_404(Paciente, pk=pk)
        print(paciente.nombre)
        signos_vitales = SignosVitales.objects.filter(paciente=paciente).all()
        self.check_object_permissions(self.request, paciente)
        return Response({'paciente': paciente, 'signos_vitales': signos_vitales})

    
    """ 
   def post(self, request, pk):
        personal_salud = get_object_or_404(PersonalSalud, pk=pk)
        serializer_context = {
            'request': request,
        }
        serializer = PersonalSaludSerilizer(personal_salud, data=request.data,context=serializer_context )
        if not serializer.is_valid():
            print("Serializador NO VALIDO")
            return Response({'serializer': serializer, 'personal_salud': personal_salud})
        serializer.save()
        return render(request, 'hospital/perfil_personal_salud.html', {'serializer': serializer, 'personal_salud': personal_salud})
"""

class PerfilPersonalSalud(APIView):
    """Solo el personal de salud proprietario tienen acceso a esta vista"""
    #permission_classes=[IsOwner, permissions.IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'hospital/perfil_personal_salud.html'

    def get(self, request, pk):
        personal_salud = get_object_or_404(PersonalSalud, pk=pk) #Datos del Usuario(Modelo PersonalSalud)
        pacientes = Paciente.objects.filter(personal_salud=personal_salud) #Pacientes asociados al personal_salid
        self.check_object_permissions(self.request, personal_salud)
        return Response({'personal_salud': personal_salud, 'pacientes': pacientes})

class SignosVitalesApi(APIView):
     
    permission_classes=[]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'hospital/signos_vitales.html'

    def get(self, request, pk):     
        signos_vitales = get_object_or_404(SignosVitales, pk=pk)
        self.check_object_permissions(self.request, signos_vitales)
        return Response({'signos_vitales': signos_vitales})

class AñadirSignosVitales(APIView):
    permission_classes=[]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'hospital/añadir_signos_vitales.html'

    def get(self, request):
        print('------------------------------GET------------------------------')
        signos_vitales = get_object_or_404(SignosVitales)
        signos_vitales.clean_fields(exclude='paciente')
#añadir signos vitales
        serializer = SignosVitalesSerilizer(signos_vitales)
        return Response({'serializer': serializer, 'signos_vitales': signos_vitales})

    def post(self, request):
        print('---------------------POST--------------------')
        serializer_context = {
            'request': request,
        }   
        signos_vitales = get_object_or_404(SignosVitales)
        serializer = SignosVitalesSerilizer(signos_vitales, data=request.data,context=serializer_context )
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'signos_vitales': signos_vitales})
        serializer.save()
        return redirect('profile-list')

#ViewSets
class HistoriaPacienteViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = HistoriaPaciente.objects.all()
    serializer_class = HistoriaPacienteSerilizer
    permission_classes = [permissions.IsAdminUser]
    search_fields = ['paciente', 'personal_salud']
    ordering_fields = '__all__'

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

