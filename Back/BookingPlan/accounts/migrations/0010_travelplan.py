# Generated by Django 5.1 on 2024-10-11 17:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_agency'),
    ]

    operations = [
        migrations.CreateModel(
            name='TravelPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure', models.CharField(max_length=100)),
                ('time', models.TimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('destination', models.CharField(max_length=100)),
                ('number_of_places', models.PositiveIntegerField()),
                ('number_of_available_places', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('complete', 'Complete'), ('active', 'Active')], default='active', max_length=10)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.agency')),
            ],
        ),
    ]