# Generated by Django 3.2.5 on 2021-09-10 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('takeouts_app', '0027_auto_20210906_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='masstakeoutconditioncommit',
            name='building',
        ),
        migrations.RemoveField(
            model_name='masstakeoutconditioncommit',
            name='building_part',
        ),
        migrations.DeleteModel(
            name='TankTakeoutCompany',
        ),
        migrations.DeleteModel(
            name='MassTakeoutConditionCommit',
        ),
    ]
