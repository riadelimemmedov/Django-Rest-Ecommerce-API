# Generated by Django 4.1.4 on 2023-05-11 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0004_productline_attribute_value_productattributevalue_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Brand",
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
                ("name", models.CharField(max_length=100, verbose_name="brand name")),
                (
                    "is_active",
                    models.BooleanField(default=False, verbose_name="is active brand"),
                ),
            ],
            options={
                "verbose_name": "Brand",
                "verbose_name_plural": "Brands",
            },
        ),
    ]
