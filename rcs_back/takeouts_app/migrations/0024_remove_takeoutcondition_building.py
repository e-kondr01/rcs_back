# Generated by Django 3.2.5 on 2021-09-05 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('takeouts_app', '0023_takeoutcondition_building_part'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='takeoutcondition',
            name='building',
        ),
    ]
