# Generated by Django 3.2.5 on 2021-09-22 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('containers_app', '0041_auto_20210910_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='precollected_mass',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='масса, собранная до старта сервиса'),
        ),
    ]
