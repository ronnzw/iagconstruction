# Generated by Django 2.0 on 2019-07-27 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='freequote',
            name='service_required',
        ),
    ]
