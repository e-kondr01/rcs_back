# Generated by Django 3.2.5 on 2021-07-19 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('takeouts_app', '0004_auto_20210719_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='tanktakeoutrequest',
            name='confirmed_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='время подтверждения'),
        ),
    ]
