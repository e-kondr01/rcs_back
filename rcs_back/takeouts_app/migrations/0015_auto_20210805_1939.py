# Generated by Django 3.2.5 on 2021-08-05 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('containers_app', '0021_auto_20210802_2117'),
        ('takeouts_app', '0014_auto_20210802_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='MassTakeoutConditionMet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='full_containers_notifications', to='containers_app.building', verbose_name='здание')),
                ('building_part', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='takeout_conditions_met', to='containers_app.buildingpart', verbose_name='корпус здания')),
            ],
            options={
                'verbose_name': 'выполнено условие для выноса',
                'verbose_name_plural': 'выполнены условия для выноса',
            },
        ),
        migrations.DeleteModel(
            name='TakeoutConditionMet',
        ),
    ]
