# Generated by Django 4.0.4 on 2022-04-13 17:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travelling_companion', '0007_rename_user1_userrelationships_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrelationships',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
