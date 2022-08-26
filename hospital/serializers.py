from hospital import views
from rest_framework import serializers
from .models import PersonalSalud,Paciente,HistoriaPaciente,SignosVitales
from django.contrib.auth.models import User

class PersonalSaludSerilizer(serializers.ModelSerializer):
    pacientes=serializers.SlugRelatedField(many=True, read_only=True, slug_field='nombre')
    class Meta:
        model = PersonalSalud
        #fields= '__all__'
        exclude = ('cargo',)

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