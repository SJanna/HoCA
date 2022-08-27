from django.contrib import admin
from .models import UsuarioFamiliar,UsuarioPaciente,UsuarioPsalud,Familiar,PersonalSalud,Paciente,HistoriaPaciente,SignosVitales
# Register your models here.
admin.site.register(PersonalSalud)
admin.site.register(Paciente)
admin.site.register(HistoriaPaciente)
admin.site.register(SignosVitales)
admin.site.register(Familiar)
admin.site.register(UsuarioFamiliar)
admin.site.register(UsuarioPsalud)
admin.site.register(UsuarioPaciente)