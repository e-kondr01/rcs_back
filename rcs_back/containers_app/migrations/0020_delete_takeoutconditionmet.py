# Generated by Django 3.2.5 on 2021-07-28 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('containers_app', '0019_container_building_part'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TakeoutConditionMet',
        ),
    ]
