# Generated by Django 3.2.5 on 2021-09-05 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('containers_app', '0037_remove_container_sticker'),
        ('takeouts_app', '0024_remove_takeoutcondition_building'),
    ]

    operations = [
        migrations.AddField(
            model_name='takeoutcondition',
            name='building',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='containers_app.building', verbose_name='здание'),
        ),
    ]
