# Generated by Django 3.2.5 on 2021-07-16 14:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('containers_app', '0012_container_capacity'),
    ]

    operations = [
        migrations.AddField(
            model_name='container',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='время добавления в систему'),
            preserve_default=False,
        ),
    ]
