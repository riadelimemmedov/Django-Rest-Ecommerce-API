# Generated by Django 4.1.4 on 2023-04-13 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductType",
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
                (
                    "name",
                    models.CharField(max_length=100, verbose_name="product type name"),
                ),
            ],
            options={
                "verbose_name": "Product Type",
                "verbose_name_plural": "Product Types",
            },
        ),
        migrations.AddField(
            model_name="productline",
            name="product_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="product.producttype",
                verbose_name="product type product line",
            ),
        ),
        migrations.CreateModel(
            name="ProductTypeAttribute",
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
                (
                    "attribute",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_type_attribute_a",
                        to="product.attribute",
                        verbose_name="product type attribute",
                    ),
                ),
                (
                    "product_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_type_attribute_pt",
                        to="product.producttype",
                        verbose_name="product type",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product Type Attribute",
                "verbose_name_plural": "Product Type Attributes",
                "unique_together": {("product_type", "attribute")},
            },
        ),
    ]
