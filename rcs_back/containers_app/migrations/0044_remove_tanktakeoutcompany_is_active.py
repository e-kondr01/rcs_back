# Generated by Django 3.2.5 on 2021-09-25 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('containers_app', '0043_building_passage_scheme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tanktakeoutcompany',
            name='is_active',
        ),
    ]
