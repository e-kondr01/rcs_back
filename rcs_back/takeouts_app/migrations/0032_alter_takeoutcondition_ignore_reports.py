# Generated by Django 3.2.5 on 2021-09-27 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('takeouts_app', '0031_alter_takeoutcondition_ignore_reports'),
    ]

    operations = [
        migrations.AlterField(
            model_name='takeoutcondition',
            name='ignore_reports',
            field=models.IntegerField(default=0, verbose_name='кол-во первых сообщений, которые нужно игнорировать'),
        ),
    ]