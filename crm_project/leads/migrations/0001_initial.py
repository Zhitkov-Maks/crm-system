# Generated by Django 5.0.2 on 2024-03-03 17:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=200, verbose_name='Имя')),
                ('phone', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'потенциальный клиент',
                'verbose_name_plural': 'потенциальные клиенты',
                'ordering': ('last_name',),
            },
        ),
    ]
