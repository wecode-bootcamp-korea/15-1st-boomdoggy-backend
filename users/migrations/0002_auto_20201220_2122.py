# Generated by Django 3.1.4 on 2020-12-20 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addresslist',
            old_name='county_region',
            new_name='country_region',
        ),
    ]