#

# Django Function
from django.db import models
from django.utils.translation import gettext_lazy as _

# Thirty Part Packages
from mptt.models import MPTTModel, TreeForeignKey


# Custom Helpers Methods
from config.helpers import random_code

# Create your models here.


#!Category
class Category(MPTTModel):
    name = models.CharField(_("category name"), max_length=100, unique=True)
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categorys"


#!Brand
class Brand(models.Model):
    name = models.CharField(_("brand name"), max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"


#!Product
class Product(models.Model):
    name = models.CharField(_("product name"), max_length=100)
    description = models.TextField(_("product description"), blank=True)
    is_digital = models.BooleanField(_("is digital product"), default=False)
    brand = models.ForeignKey(
        Brand, verbose_name=_("product brand"), on_delete=models.CASCADE
    )
    category = TreeForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, blank=True
    )
    is_active = models.BooleanField(_("is active product"), default=False)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


#!ProductLine
class ProductLine(models.Model):
    price = models.DecimalField(_("price"), decimal_places=2, max_digits=5)
    sku = models.CharField(
        _("universal product code"),
        max_length=50,
        db_index=True,
        null=True,
        blank=True,
        unique=True,
    )
    stock_qty = models.IntegerField(_("stock quantity"), default=0)
    product = models.ForeignKey(
        Product, verbose_name="product", on_delete=models.CASCADE
    )
    is_active = models.BooleanField(_("is active productline"), default=False)

    class Meta:
        verbose_name = "ProductLine"
        verbose_name_plural = "ProductLines"

    def __str__(self):
        return f"{self.product.name} - {self.price} - {self.sku}"

    def save(self, *args, **kwargs):
        self.sku = random_code()
        super(ProductLine, self).save(*args, **kwargs)
