# Generated by Django 5.0.2 on 2024-03-05 19:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
        ('customers', '0002_customers_contract_alter_customers_lead'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contracts', to='contracts.contracts'),
        ),
    ]
