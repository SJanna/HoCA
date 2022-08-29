from rest_framework import serializers
from .models import Familiar, PersonalSalud,Paciente,HistoriaPaciente,SignosVitales
from django.contrib.auth.models import User

class PersonalSaludSerilizer(serializers.ModelSerializer):
    pacientes=serializers.SlugRelatedField(many=True, read_only=True, slug_field='nombre')
    class Meta:
        model = PersonalSalud
        fields='__all__'

class PacienteSerilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paciente
        fields= '__all__'

class HistoriaPacienteSerilizer(serializers.ModelSerializer):
    doctor = serializers.SerializerMethodField('_doctor')
    def _doctor(self, obj):
        request = self.context.get('request', None)
        try:
            if request:
                usuario=request.user.id
                doctor=PersonalSalud.objects.get(usuario=usuario)
                return str(doctor.id)
        except:
            pass    
    class Meta:
        model = HistoriaPaciente
        fields = '__all__'

class SignosVitalesSerilizer(serializers.ModelSerializer):
    paciente = serializers.SerializerMethodField('_paciente')
    def _paciente(self, obj):
        request = self.context.get('request', None)
        try:
            if request:
                usuario=request.user.id
                paciente=Paciente.objects.get(usuario=usuario)
                return str(paciente.id)
        except:
            pass

    class Meta:   
        model = SignosVitales
        fields = '__all__'

class FamiliarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Familiar
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email', 'username', 'password','groups','is_active']
        #extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data): #Para cifrar la contraseña
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user