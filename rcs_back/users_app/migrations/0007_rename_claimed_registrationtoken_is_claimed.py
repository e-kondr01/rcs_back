# Generated by Django 3.2.5 on 2021-08-22 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0006_registrationtoken'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrationtoken',
            old_name='claimed',
            new_name='is_claimed',
        ),
    ]
