# Generated by Django 5.0.2 on 2024-03-08 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0004_leads_middle_name_alter_leads_advertising_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='leads',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='активный клиент'),
        ),
    ]
