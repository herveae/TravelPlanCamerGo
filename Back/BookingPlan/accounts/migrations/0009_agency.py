# Generated by Django 5.1 on 2024-10-02 14:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_delete_agency'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='image/agency/')),
                ('description', models.TextField()),
                ('agency_receptionist', models.ForeignKey(limit_choices_to={'roles': 'agency_receptionist'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='managed_agencies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
