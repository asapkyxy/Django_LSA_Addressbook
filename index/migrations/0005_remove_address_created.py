# Generated by Django 4.0.5 on 2022-06-05 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_rename_firstname_address_fname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='created',
        ),
    ]
