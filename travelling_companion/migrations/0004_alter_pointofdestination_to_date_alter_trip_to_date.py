# Generated by Django 4.0.4 on 2022-04-13 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelling_companion', '0003_alter_userrelationships_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointofdestination',
            name='to_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='trip',
            name='to_date',
            field=models.DateField(),
        ),
    ]