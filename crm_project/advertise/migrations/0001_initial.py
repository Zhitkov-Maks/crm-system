# Generated by Django 5.0.2 on 2024-03-03 17:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Компания')),
                ('budget', models.DecimalField(decimal_places=2, max_digits=14, verbose_name='Бюджет')),
                ('promotion_channel', models.CharField(max_length=200, verbose_name='Канал продвижения')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='products.products', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'advertise',
                'verbose_name_plural': 'advertises',
                'ordering': ('budget',),
            },
        ),
    ]