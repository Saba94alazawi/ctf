# Generated by Django 4.0.3 on 2022-09-20 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fines', '0008_remove_deviceinfo_deviceip'),
    ]

    operations = [
        migrations.AddField(
            model_name='deviceinfo',
            name='update',
            field=models.TimeField(auto_now=True),
        ),
    ]