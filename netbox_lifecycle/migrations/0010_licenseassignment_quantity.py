# Generated by Django 4.1.7 on 2023-05-16 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_lifecycle', '0009_alter_licenseassignment_device'),
    ]

    operations = [
        migrations.AddField(
            model_name='licenseassignment',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
