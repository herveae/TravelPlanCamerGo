# Generated by Django 5.1 on 2024-10-01 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_customuser_accommodation_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='role',
            new_name='roles',
        ),
    ]
