# Generated by Django 4.1 on 2022-08-27 12:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hospital', '0005_alter_personalsalud_registro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariofamiliar',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='familiar', to=settings.AUTH_USER_MODEL),
        ),
    ]
