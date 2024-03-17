# Generated by Django 5.0.2 on 2024-03-04 18:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertise', '0002_remove_advertise_product_advertise_product'),
        ('products', '0002_alter_products_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertise',
            name='product',
        ),
        migrations.AddField(
            model_name='advertise',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='services', to='products.products', verbose_name='Услуга'),
            preserve_default=False,
        ),
    ]
