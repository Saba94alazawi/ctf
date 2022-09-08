# Generated by Django 4.1 on 2022-08-09 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fines', '0005_deviceinfo_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deviceinfo',
            name='time',
        ),
        migrations.AddField(
            model_name='deviceinfo',
            name='deviceIP',
            field=models.GenericIPAddressField(null=True),
        ),
    ]
