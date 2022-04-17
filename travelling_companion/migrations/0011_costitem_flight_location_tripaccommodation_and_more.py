# Generated by Django 4.0.4 on 2022-04-15 07:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travelling_companion', '0010_trip_cost_alter_pointofdestination_trip_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CostItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_time', models.DateTimeField()),
                ('checked', models.BooleanField(default=False)),
                ('cost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelling_companion.costitem')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TripAccommodation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('cost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelling_companion.costitem')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='travelling_companion.location')),
            ],
        ),
        migrations.CreateModel(
            name='TripPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted', models.BooleanField(default=True)),
                ('approved', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='pointofdestination',
            name='city',
        ),
        migrations.RemoveField(
            model_name='pointofdestination',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='pointofdestination',
            name='trip',
        ),
        migrations.RemoveField(
            model_name='traveler',
            name='home_city',
        ),
        migrations.RemoveField(
            model_name='traveler',
            name='passport',
        ),
        migrations.RemoveField(
            model_name='traveler',
            name='person',
        ),
        migrations.RemoveField(
            model_name='traveler',
            name='user',
        ),
        migrations.RemoveField(
            model_name='triptravelers',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='triptravelers',
            name='traveler',
        ),
        migrations.RemoveField(
            model_name='triptravelers',
            name='trip',
        ),
        migrations.RenameField(
            model_name='passport',
            old_name='owner',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='owner',
            new_name='created_by',
        ),
        migrations.RenameField(
            model_name='userrelationships',
            old_name='recipient',
            new_name='user2',
        ),
        migrations.AlterUniqueTogether(
            name='userrelationships',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='person',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='cost',
        ),
        migrations.AddField(
            model_name='person',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='passport',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='travelling_companion.passport'),
        ),
        migrations.AddField(
            model_name='person',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='trip',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userrelationships',
            name='user1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trip',
            name='budget',
            field=models.FloatField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='userrelationships',
            unique_together={('user1', 'user2')},
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='PointOfDestination',
        ),
        migrations.DeleteModel(
            name='Traveler',
        ),
        migrations.DeleteModel(
            name='TripTravelers',
        ),
        migrations.AddField(
            model_name='tripperson',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelling_companion.person'),
        ),
        migrations.AddField(
            model_name='tripperson',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelling_companion.trip'),
        ),
        migrations.AddField(
            model_name='tripaccommodation',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelling_companion.trip'),
        ),
        migrations.AddField(
            model_name='flight',
            name='from_dest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='from_dest', to='travelling_companion.location'),
        ),
        migrations.AddField(
            model_name='flight',
            name='to_dest',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='to_dest', to='travelling_companion.location'),
        ),
        migrations.AddField(
            model_name='flight',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelling_companion.trip'),
        ),
        migrations.AddField(
            model_name='costitem',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelling_companion.trip'),
        ),
        migrations.RemoveField(
            model_name='userrelationships',
            name='owner',
        ),
        migrations.AddField(
            model_name='trip',
            name='trip_location',
            field=models.ManyToManyField(to='travelling_companion.location'),
        ),
    ]