# Generated by Django 4.1 on 2022-08-29 04:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('numero_id', models.IntegerField()),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=30)),
                ('fecha_nacimiento', models.DateField(max_length=30)),
                ('telefono', models.CharField(max_length=13)),
                ('genero', models.CharField(choices=[('M', 'MASCULINO'), ('F', 'FEMENINO'), ('NB', 'NO BINARIO')], max_length=10)),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
        ),
        migrations.CreateModel(
            name='SignosVitales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('oximetria', models.IntegerField(blank=True, null=True)),
                ('frecuencia_respiratoria', models.IntegerField(blank=True, null=True)),
                ('frecuencia_cardiaca', models.IntegerField(blank=True, null=True)),
                ('tempreratura', models.IntegerField(blank=True, null=True)),
                ('presion_arterial', models.IntegerField(blank=True, null=True)),
                ('glicemias', models.IntegerField(blank=True, null=True)),
                ('paciente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mis_signos_vitales', to='hospital.paciente')),
            ],
            options={
                'verbose_name': 'SignosVitales',
            },
        ),
        migrations.CreateModel(
            name='PersonalSalud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('numero_id', models.IntegerField()),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=13)),
                ('especialidad', models.CharField(max_length=50)),
                ('registro', models.FileField(blank=True, null=True, upload_to='hospital/registros/')),
                ('genero', models.CharField(choices=[('MASCULINO', 'M'), ('FEMENINO', 'F'), ('No Binario', 'NB')], max_length=10)),
                ('cargo', models.CharField(choices=[('MEDICO', 'Medico'), ('ENFERMERO', 'Enfermero')], max_length=9)),
                ('usuario', models.OneToOneField(blank=True, limit_choices_to={'groups': 2}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuario_p_salud', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'PersonalSalud',
            },
        ),
        migrations.AddField(
            model_name='paciente',
            name='personal_salud',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pacientes', to='hospital.personalsalud'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='usuario',
            field=models.OneToOneField(blank=True, limit_choices_to={'groups': 3}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='paciente_usuario', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='HistoriaPaciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comentario', models.TextField()),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medico_historia', to='hospital.personalsalud')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente_historia', to='hospital.paciente')),
            ],
            options={
                'verbose_name': 'HistoriaPaciente',
                'verbose_name_plural': 'HistoriaPacientes',
            },
        ),
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('numero_id', models.IntegerField()),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=13)),
                ('genero', models.CharField(choices=[('MASCULINO', 'M'), ('FEMENINO', 'F'), ('No Binario', 'NB')], max_length=10)),
                ('correo', models.EmailField(max_length=254)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='familiar_paciente', to='hospital.paciente')),
                ('usuario', models.OneToOneField(blank=True, limit_choices_to={'groups': 4}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='familiar_usuario', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'familiar',
                'verbose_name_plural': 'familiares',
            },
        ),
        migrations.CreateModel(
            name='auxiliar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('numero_id', models.IntegerField()),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=13)),
                ('genero', models.CharField(choices=[('MASCULINO', 'M'), ('FEMENINO', 'F'), ('No Binario', 'NB')], max_length=10)),
                ('usuario', models.OneToOneField(blank=True, limit_choices_to={'groups': 2}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuario_auxiliar', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Auxiliar',
                'verbose_name_plural': 'Auxiliares',
            },
        ),
    ]
