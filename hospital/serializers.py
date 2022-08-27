from hospital import views
from rest_framework import serializers
from .models import UsuarioPaciente,UsuarioFamiliar,UsuarioPsalud,Familiar, PersonalSalud,Paciente,HistoriaPaciente,SignosVitales
from django.contrib.auth.models import User

class PersonalSaludSerilizer(serializers.HyperlinkedModelSerializer):
    pacientes=serializers.SlugRelatedField(many=True, read_only=True, slug_field='nombre')
    class Meta:
        model = PersonalSalud
        #fields= '__all__'
        exclude = ('cargo',)

class PacienteSerilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paciente
        fields= '__all__'

class HistoriaPacienteSerilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HistoriaPaciente
        fields = '__all__'

class SignosVitalesSerilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SignosVitales
        fields = '__all__'

class FamiliarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Familiar
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email',
              'is_active', 'is_staff', 'is_superuser', 'password',)

        # These fields are displayed but not editable and have to be a part of 'fields' tuple
        read_only_fields = ('is_staff', 'is_superuser',)

        # These fields are only editable (not displayed) and have to be a part of 'fields' tuple
        extra_kwargs = {'password': {'write_only': True, 'min_length': 4}}

class UsuarioPacienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=UsuarioPaciente
        fields= '__all__'

class UsuarioPsaludSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=UsuarioPsalud
        fields= '__all__'

class UsuarioFamiliarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=UsuarioFamiliar
        fields= '__all__'