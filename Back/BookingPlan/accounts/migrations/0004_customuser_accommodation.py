# Generated by Django 5.1 on 2024-09-30 15:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_accommodation_agency_destination_hotel_booking_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='accommodation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.accommodation'),
        ),
    ]