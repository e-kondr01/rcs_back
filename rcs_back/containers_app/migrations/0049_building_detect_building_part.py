# Generated by Django 3.2.5 on 2021-10-12 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('containers_app', '0048_auto_20211012_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='detect_building_part',
            field=models.BooleanField(default=False, verbose_name='определять номер корпуса по аудитории'),
        ),
    ]
