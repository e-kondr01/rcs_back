# Generated by Django 3.2.5 on 2021-07-15 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('containers_app', '0010_auto_20210715_2021'),
        ('takeouts_app', '0002_auto_20210707_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContainersTakeoutConfirmation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('worker_info', models.CharField(max_length=2048, verbose_name='информация о рабочем')),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='confirmations', to='containers_app.building', verbose_name='здание')),
                ('containers', models.ManyToManyField(related_name='takeout_confirmations', to='containers_app.Container', verbose_name='контейнеры подтверждённые пустыми')),
            ],
            options={
                'verbose_name': 'подтверждение выноса контейнеров',
                'verbose_name_plural': 'подтверждения выносов контейнеров',
            },
        ),
        migrations.CreateModel(
            name='ContainersTakeoutRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('confirmed', models.BooleanField(default=False, verbose_name='подтверждён')),
                ('containers', models.ManyToManyField(related_name='takeout_requests', to='containers_app.Container', verbose_name='выбранные для выноса контейнеры')),
            ],
            options={
                'verbose_name': 'запрос выноса контейнеров',
                'verbose_name_plural': 'запросы выноса контейнеров',
            },
        ),
        migrations.CreateModel(
            name='TankTakeoutRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tank_takeout_requests', to='containers_app.building', verbose_name='здание')),
            ],
            options={
                'verbose_name': 'запрос вывоза бака',
                'verbose_name_plural': 'запросы вывоза баков',
            },
        ),
        migrations.DeleteModel(
            name='EnoughFullContainersNotification',
        ),
        migrations.DeleteModel(
            name='TakeoutRequest',
        ),
    ]