# Generated by Django 3.1.4 on 2020-12-23 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20201222_0254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carts',
            name='sub_total',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='option',
        ),
    ]
