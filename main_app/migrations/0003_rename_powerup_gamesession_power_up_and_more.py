# Generated by Django 5.1.1 on 2024-10-07 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_gamesession'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gamesession',
            old_name='powerUp',
            new_name='power_up',
        ),
        migrations.AlterField(
            model_name='gamesession',
            name='date',
            field=models.DateField(verbose_name='Game Date'),
        ),
    ]
