# Generated by Django 4.2.4 on 2023-09-12 16:43

from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Имя категории')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание категории')),
                ('slug', models.SlugField(editable=False, max_length=70, unique=True, verbose_name='URL-имя')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Имя подкатегории')),
                ('slug', models.SlugField(editable=False, max_length=70, unique=True, verbose_name='URL-имя')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='categories', to='products.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Подкатегория',
                'verbose_name_plural': 'Подкатегории',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Название товара')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание товара')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена товара')),
                ('slug', models.SlugField(editable=False, max_length=148, unique=True, verbose_name='URL-имя')),
                ('is_available', models.BooleanField(default=True, verbose_name='Доступность товара')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата добавления товара')),
                ('image', models.ImageField(blank=True, null=True, upload_to=products.models.create_directory_path, verbose_name='Изображение товара')),
                ('category', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='products.category', verbose_name='Категория')),
                ('subcategory', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='subcategory', to='products.subcategory', verbose_name='Подкатегория')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['name', '-price'],
            },
        ),
    ]
