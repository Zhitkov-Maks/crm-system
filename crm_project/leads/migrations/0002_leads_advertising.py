# Generated by Django 5.0.2 on 2024-03-04 18:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertise', '0002_remove_advertise_product_advertise_product'),
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leads',
            name='advertising',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.PROTECT, to='advertise.advertise', verbose_name='кампания'),
            preserve_default=False,
        ),
    ]