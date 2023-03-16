#

#!Django Function
from django.db import models
from django.utils.translation import gettext_lazy as _

#!Thirty Part Packages
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


#!Category
class Category(MPTTModel):
    name = models.CharField(_("category name"), max_length=100)
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categorys"


#!Brand
class Brand(models.Model):
    name = models.CharField(_("brand name"), max_length=100)

    def __str__(self):
        return str(self.name)

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

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
