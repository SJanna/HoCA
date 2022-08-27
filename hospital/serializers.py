from rest_framework import serializers
from .models import Familiar, PersonalSalud,Paciente,HistoriaPaciente,SignosVitales
from django.contrib.auth.models import User

class PersonalSaludSerilizer(serializers.HyperlinkedModelSerializer):
    pacientes=serializers.SlugRelatedField(many=True, read_only=True, slug_field='nombre')
    class Meta:
        model = PersonalSalud
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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user