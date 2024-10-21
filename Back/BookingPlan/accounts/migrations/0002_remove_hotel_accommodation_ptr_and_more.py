# Generated by Django 5.1 on 2024-09-28 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='accommodation_ptr',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='accommodation',
        ),
        migrations.DeleteModel(
            name='Agency',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
        migrations.DeleteModel(
            name='Destination',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Hotel',
        ),
        migrations.DeleteModel(
            name='Accommodation',
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]