from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Medico(TimeStampMixin):
    usuario = models.OneToOneField(User,related_name='usuario_medico', on_delete=models.CASCADE)
    edad=models.IntegerField()
    direccion=models.CharField(max_length=50)
    telefono=models.CharField(max_length=13)

    class Meta:
        verbose_name = "Medico"
        verbose_name_plural = "Medicos"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Medico_detail", kwargs={"pk": self.pk})

class SignosVitales(TimeStampMixin):
    oximetria=models.IntegerField(blank=True, null=True)
    frecuencia_respiratoria=models.IntegerField(blank=True, null=True)
    frecuencia_cardiaca=models.IntegerField(blank=True, null=True)
    tempreratura=models.IntegerField(blank=True, null=True)
    presion_arterial=models.IntegerField(blank=True, null=True)
    glicemias=models.IntegerField(blank=True, null=True)
    

    class Meta:
        verbose_name = "SignosVitales"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("SignosVitales_detail", kwargs={"pk": self.pk})

class Paciente(TimeStampMixin):
    usuario=models.OneToOneField(User,related_name='usuario_paciente', on_delete=models.CASCADE)
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=30)
    medico=models.ForeignKey(Medico,default="Medico no asignado", related_name='mi_medico_asignado', on_delete=models.SET_DEFAULT)
    signos_vitales=models.ForeignKey(SignosVitales, related_name='mis_signos_vitales', on_delete=models.CASCADE)
    

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Paciente_detail", kwargs={"pk": self.pk})

class HistoriaPaciente(TimeStampMixin):
    paciente=models.ForeignKey(Paciente, related_name='paciente_historia', on_delete=models.CASCADE)
    doctor=models.ForeignKey(Paciente, related_name='medico_historia', on_delete=models.CASCADE)
    comentario=models.TextField()

    class Meta:
        verbose_name = "HistoriaPaciente"
        verbose_name_plural = "HistoriaPacientes"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("HistoriaPaciente_detail", kwargs={"pk": self.pk})
