# Generated by Django 5.0.2 on 2024-03-18 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Products",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200, verbose_name="Услуга")),
                (
                    "description",
                    models.TextField(max_length=3000, verbose_name="Описание"),
                ),
                (
                    "cost",
                    models.DecimalField(
                        decimal_places=2, max_digits=14, verbose_name="Цена"
                    ),
                ),
            ],
            options={
                "verbose_name": "Услуга",
                "verbose_name_plural": "Услуги",
                "ordering": ("name",),
            },
        ),
    ]
