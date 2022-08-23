from hospital import views
from rest_framework import serializers
from .models import Medico,Paciente,HistoriaPaciente,SignosVitales
from django.contrib.auth.models import User

class MedicoSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'

class PacienteSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'

class HistoriaPacienteSerilizer(serializers.ModelSerializer):
    class Meta:
        model = HistoriaPaciente
        fields = '__all__'

class SignosVitalesSerilizer(serializers.ModelSerializer):
    class Meta:
        model = SignosVitales
        fields = '__all__'