# Generated by Django 4.1.4 on 2023-04-30 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_alter_productline_created_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="product_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="product.producttype",
                verbose_name="product type",
            ),
        ),
        migrations.AddField(
            model_name="productline",
            name="product_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="product.producttype",
                verbose_name="product type",
            ),
        ),
        migrations.AddField(
            model_name="producttype",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="product.producttype",
            ),
        ),
    ]
