<<<<<<< HEAD
# Generated by Django 3.1.4 on 2020-12-21 17:54
=======
# Generated by Django 3.1.4 on 2020-12-21 17:33
# Generated by Django 3.1.4 on 2020-12-21 08:44
>>>>>>> main

from django.db import migrations, models
import django.db.models.deletion
import validation


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('appartment_type', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=200, validators=[validation.validate_city])),
                ('county_region', models.CharField(max_length=100)),
                ('postcode', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50, validators=[validation.validate_phone])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users')),
            ],
            options={
                'db_table': 'payments',
            },
        ),
        migrations.CreateModel(
            name='PaymentsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payments_module_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'payments_type',
            },
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('shipping_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.orders')),
            ],
            options={
                'db_table': 'shipping',
            },
        ),
        migrations.CreateModel(
            name='PaymentsCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.payments')),
                ('payments_types', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payments.paymentstype')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users')),
            ],
            options={
                'db_table': 'payments_card',
            },
        ),
    ]
