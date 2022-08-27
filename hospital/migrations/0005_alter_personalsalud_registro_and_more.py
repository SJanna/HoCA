# Generated by Django 4.1 on 2022-08-27 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hospital', '0004_alter_personalsalud_registro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalsalud',
            name='registro',
            field=models.FileField(upload_to='hospital/registros/'),
        ),
        migrations.AlterField(
            model_name='usuariofamiliar',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='familiar', to=settings.AUTH_USER_MODEL),
        ),
    ]