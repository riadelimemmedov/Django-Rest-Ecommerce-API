# Generated by Django 4.1.4 on 2023-04-05 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_productimage"),
    ]

    operations = [
        migrations.CreateModel(
            name="Attribute",
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
                    models.CharField(max_length=100, verbose_name="attribute name"),
                ),
                (
                    "description",
                    models.TextField(blank=True, verbose_name="attribute description"),
                ),
            ],
            options={
                "verbose_name": "Attribute",
                "verbose_name_plural": "Attributes",
            },
        ),
        migrations.CreateModel(
            name="AttributeValue",
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
                    "attr_value",
                    models.CharField(max_length=100, verbose_name="attr value"),
                ),
                (
                    "attribute",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attribute_value",
                        to="product.attribute",
                        verbose_name="attribute",
                    ),
                ),
            ],
            options={
                "verbose_name": "AttributeValue",
                "verbose_name_plural": "AttributeValues",
            },
        ),
        migrations.AlterField(
            model_name="productimage",
            name="product_image_url",
            field=models.ImageField(
                default="test.png", upload_to="image/", verbose_name="product image url"
            ),
        ),
        migrations.CreateModel(
            name="ProductLineAttributeValue",
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
                    "attr_value",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_attr_value_av",
                        to="product.attributevalue",
                        verbose_name="product line attribute value",
                    ),
                ),
                (
                    "product_line",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_attr_value_pl",
                        to="product.productline",
                        verbose_name="product line",
                    ),
                ),
            ],
            options={
                "unique_together": {("attr_value", "product_line")},
            },
        ),
        migrations.AddField(
            model_name="productline",
            name="attribute_value",
            field=models.ManyToManyField(
                null=True,
                through="product.ProductLineAttributeValue",
                to="product.attributevalue",
            ),
        ),
    ]