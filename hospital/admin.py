from django.contrib import admin
from .models import PersonalSalud,Paciente,HistoriaPaciente,SignosVitales
# Register your models here.
admin.site.register(PersonalSalud)
admin.site.register(Paciente)
admin.site.register(HistoriaPaciente)
admin.site.register(SignosVitales)