# Generated by Django 3.1.4 on 2020-12-23 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_merge_20201223_1949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='options',
            name='product',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='option',
        ),
        migrations.AlterField(
            model_name='carts',
            name='sub_total',
            field=models.IntegerField(default=0),
        ),
    ]