# Generated by Django 3.2.5 on 2021-08-26 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('containers_app', '0033_auto_20210826_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='container',
            name='avg_fill_time',
        ),
        migrations.RemoveField(
            model_name='container',
            name='avg_takeout_wait_time',
        ),
    ]
