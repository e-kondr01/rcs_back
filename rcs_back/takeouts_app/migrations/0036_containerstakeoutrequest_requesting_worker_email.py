# Generated by Django 3.2.5 on 2021-11-30 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('takeouts_app', '0035_containerstakeoutrequest_archive_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='containerstakeoutrequest',
            name='requesting_worker_email',
            field=models.CharField(blank=True, max_length=64, verbose_name='email сотрудника (архив)'),
        ),
    ]