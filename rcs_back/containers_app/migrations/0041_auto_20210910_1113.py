# Generated by Django 3.2.5 on 2021-09-10 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('containers_app', '0040_auto_20210907_1755'),
    ]

    operations = [
        migrations.CreateModel(
            name='TankTakeoutCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('is_active', models.BooleanField(default=True, verbose_name='активна')),
            ],
            options={
                'verbose_name': 'компания, вывоза бака',
                'verbose_name_plural': 'компании, вывоз бака',
            },
        ),
        migrations.AddField(
            model_name='building',
            name='_takeout_notified',
            field=models.BooleanField(default=False, verbose_name='послано оповещение о необходимоси сбора'),
        ),
    ]
