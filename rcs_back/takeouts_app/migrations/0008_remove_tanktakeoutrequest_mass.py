# Generated by Django 3.2.5 on 2021-07-20 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('takeouts_app', '0007_tanktakeoutrequest_mass'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tanktakeoutrequest',
            name='mass',
        ),
    ]
