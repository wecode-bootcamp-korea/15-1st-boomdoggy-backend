# Generated by Django 3.1.4 on 2020-12-17 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=2000)),
            ],
            options={
                'db_table': 'images',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('review_rating', models.SmallIntegerField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=3)),
                ('piece', models.CharField(blank=True, max_length=100)),
                ('kilogram', models.CharField(blank=True, max_length=100)),
                ('quantity', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=1000)),
                ('benefit', models.CharField(max_length=1000)),
                ('ingredients', models.CharField(max_length=1000)),
                ('stock_rate', models.IntegerField(default=0)),
                ('sale_rate', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categories')),
                ('subscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.subscription')),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content', models.CharField(max_length=1000)),
                ('review_rating', models.IntegerField(default=0)),
                ('image_url', models.CharField(max_length=500)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categories')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products')),
            ],
            options={
                'db_table': 'reviews',
            },
        ),
        migrations.CreateModel(
            name='ImagesProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products')),
            ],
            options={
                'db_table': 'images_products',
            },
        ),
        migrations.AddField(
            model_name='images',
            name='image',
            field=models.ManyToManyField(through='products.ImagesProducts', to='products.Products'),
        ),
    ]
