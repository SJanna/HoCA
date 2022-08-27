from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class UsuarioPaciente(TimeStampMixin):
    usuario=models.OneToOneField(User,related_name='usuario_paciente', on_delete=models.CASCADE)
    def __str__(self):
        return self.usuario.username

class UsuarioPsalud(TimeStampMixin):
    usuario=models.OneToOneField(User,related_name='usuario_personal_salud', on_delete=models.CASCADE)
    def __str__(self):
        return self.usuario.username

class UsuarioFamiliar(TimeStampMixin):
    usuario=models.OneToOneField(User,related_name='usuario_familiar', on_delete=models.CASCADE)
    def __str__(self):
        return self.usuario.username

class PersonalSalud(TimeStampMixin):
    numero_id=models.IntegerField()
    usuario = models.OneToOneField(UsuarioPsalud,related_name='usuario_p_salud', on_delete=models.CASCADE, null=True, blank=True)
    nombre=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=50)
    telefono=models.CharField(max_length=13)
    especialidad=models.CharField(max_length=50)
    registro=models.FileField(upload_to =f'hospital/registros/')
    genero=models.CharField(choices=[('MASCULINO','M'),('FEMENINO','F'),('No Binario','NB'),] ,max_length=10)
    CARGO = [
        ('MEDICO', 'Medico'),
        ('ENFERMERO', 'Enfermero'),]
    cargo=models.CharField(max_length=9, choices=[('MEDICO','Medico'),('ENFERMERO','Enfermero')])

    class Meta:
        verbose_name = "PersonalSalud"

    def __str__(self):
        return self.nombre + " " + self.apellidos

    def get_absolute_url(self):
        return reverse("PersonalSalud_detail", kwargs={"pk": self.pk})

class Paciente(TimeStampMixin):
    numero_id=models.IntegerField()
    usuario=models.OneToOneField(UsuarioPaciente,related_name='paciente_usuario', on_delete=models.CASCADE, blank=True, null=True)
    nombre=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=50)
    direccion=models.CharField(max_length=30)
    ciudad=models.CharField(max_length=30)
    fecha_nacimiento=models.DateField(max_length=30)
    telefono=models.CharField(max_length=13)
    genero=models.CharField(choices=[('M','MASCULINO'),('F','FEMENINO'),('NB','NO BINARIO'),] ,max_length=10)
    personal_salud=models.ForeignKey(PersonalSalud, related_name='pacientes', on_delete=models.SET_NULL, null=True, blank=True)    

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __str__(self):
        return self.nombre + " " + self.apellidos

    def get_absolute_url(self):
        return reverse("Paciente_detail", kwargs={"pk": self.pk})

class HistoriaPaciente(TimeStampMixin):
    paciente=models.ForeignKey(Paciente, related_name='paciente_historia', on_delete=models.CASCADE)
    doctor=models.ForeignKey(Paciente, related_name='medico_historia', on_delete=models.CASCADE)
    comentario=models.TextField()

    class Meta:
        verbose_name = "HistoriaPaciente"
        verbose_name_plural = "HistoriaPacientes"

    def get_absolute_url(self):
        return reverse("HistoriaPaciente_detail", kwargs={"pk": self.pk})

class SignosVitales(TimeStampMixin):
    oximetria=models.IntegerField(blank=True, null=True)
    frecuencia_respiratoria=models.IntegerField(blank=True, null=True)
    frecuencia_cardiaca=models.IntegerField(blank=True, null=True)
    tempreratura=models.IntegerField(blank=True, null=True)
    presion_arterial=models.IntegerField(blank=True, null=True)
    glicemias=models.IntegerField(blank=True, null=True)
    paciente=models.ForeignKey(Paciente, related_name='mis_signos_vitales', on_delete=models.CASCADE)


    class Meta:
        verbose_name = "SignosVitales"

    def get_absolute_url(self):
        return reverse("SignosVitales_detail", kwargs={"pk": self.pk})

class auxiliar(TimeStampMixin):
    numero_id=models.IntegerField()
    usuario = models.OneToOneField(User,related_name='usuario_auxiliar', on_delete=models.CASCADE, null=True, blank=True)
    nombre=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=50)
    telefono=models.CharField(max_length=13)
    genero=models.CharField(choices=[('MASCULINO','M'),('FEMENINO','F'),('No Binario','NB'),] ,max_length=10)

    class Meta:
        verbose_name = "Auxiliar"
        verbose_name_plural = "Auxiliares"

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("Auxiliar_detail", kwargs={"pk": self.pk})

class Familiar(TimeStampMixin):
    numero_id=models.IntegerField()
    usuario=models.OneToOneField(UsuarioFamiliar,related_name='familiar_usuario', on_delete=models.CASCADE, blank=True, null=True)
    nombre=models.CharField(max_length=30)
    apellidos=models.CharField(max_length=50)
    telefono=models.CharField(max_length=13)
    genero=models.CharField(choices=[('MASCULINO','M'),('FEMENINO','F'),('No Binario','NB'),] ,max_length=10)
    correo=models.EmailField()
    paciente=models.ForeignKey(Paciente, related_name='familiar_paciente', on_delete=models.CASCADE)
        
    class Meta:
        verbose_name = "familiar"
        verbose_name_plural = "familiares"

    def __str__(self):
        return self.nombre + " " + self.apellidos

    def get_absolute_url(self):
        reverse("Familiar_detail", kwargs={"pk": self.pk})