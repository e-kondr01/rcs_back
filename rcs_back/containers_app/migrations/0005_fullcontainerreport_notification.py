# Generated by Django 3.2.5 on 2021-07-06 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('takeouts_app', '0001_initial'),
        ('containers_app', '0004_auto_20210706_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='fullcontainerreport',
            name='notification',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='containers', to='takeouts_app.fullcontainersnotification', verbose_name='оповещение о полных контейнерах'),
        ),
    ]
