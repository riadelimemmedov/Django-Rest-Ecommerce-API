#

# Django Function
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from .fields import *

# Thirty Part Packages
from mptt.models import MPTTModel, TreeForeignKey
from djmoney.models.fields import MoneyField
from django_extensions.db.fields import RandomCharField
from django_extensions.db.models import ActivatorModel, TimeStampedModel


# Custom Helpers Methods
from config.helpers import random_code, returnFlugFormat

# Create your models here.


# *ActiveQueryset
class ActiveQueryset(models.QuerySet):
    # def get_queryset(self):#if using get_queryset override default django objects models and create some collision when write orm query
    #     return super().get_queryset().filter(is_active=True)

    def get_is_active(self):
        return self.filter(is_active=True)


####################################################################################################################################################################

#!Category
class Category(MPTTModel):
    name = models.CharField(_("category name"), max_length=235, unique=True)
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)
    is_active = models.BooleanField(_("is active category"), default=False)
    ctg_slug = models.SlugField(
        _("category slug"), max_length=255, unique=True, db_index=True, blank=True
    )

    objects = ActiveQueryset.as_manager()

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.ctg_slug = returnFlugFormat(f"{self.name}")
        super(Category, self).save(*args, **kwargs)

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categorys"


#!Product
class Product(TimeStampedModel):
    name = models.CharField(_("product name"), max_length=100)
    description = models.TextField(_("product description"), blank=True)
    is_digital = models.BooleanField(_("is digital product"), default=False)
    pid = RandomCharField(
        _("product unique id"), length=10, unique=True, db_index=True, null=True
    )
    # brand = models.ForeignKey(
    #     Brand, verbose_name=_("product brand"), on_delete=models.CASCADE
    # )
    category = TreeForeignKey(
        "Category", on_delete=models.PROTECT, null=True, blank=True
    )
    pr_slug = models.SlugField(
        _("product slug"), max_length=255, unique=True, db_index=True, blank=True
    )
    is_active = models.BooleanField(_("is active product"), default=False)
    # product_type = models.ForeignKey(
    #     "ProductType",
    #     verbose_name="product type",
    #     on_delete=models.PROTECT,
    #     null=True,
    # )

    # => if you want add new query methods to django objects model
    objects = ActiveQueryset.as_manager()

    # active_objects = ProductManager() #=> if you create seperate manager,

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        self.pr_slug = returnFlugFormat(f"{self.name}")
        super(Product, self).save(*args, **kwargs)


#!Attribute
class Attribute(models.Model):
    name = models.CharField(_("attribute name"), max_length=100)
    description = models.TextField(_("attribute description"), blank=True)

    class Meta:
        verbose_name = "Attribute"
        verbose_name_plural = "Attributes"

    def __str__(self):
        return str(self.name)


#!AttributeValue
class AttributeValue(models.Model):
    attr_value = models.CharField(_("attr value"), max_length=100)
    attribute = models.ForeignKey(
        Attribute,
        verbose_name="attribute",
        on_delete=models.CASCADE,
        related_name="attribute_value",
    )

    class Meta:
        verbose_name = "AttributeValue"
        verbose_name_plural = "AttributeValues"

    def __str__(self):
        return f"{self.attr_value} --- {self.attribute.name}"


#!ProductLine
class ProductLine(models.Model):
    price = MoneyField(
        _("price"), decimal_places=2, max_digits=10, default_currency="USD"
    )
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
        Product,
        related_name="products",
        verbose_name="product",
        on_delete=models.PROTECT,
    )
    is_active = models.BooleanField(_("is active productline"), default=False)
    order = OrderField(unique_for_field="product", blank=True, null=True)
    weight = models.FloatField(_("product weight"), default=0)
    # attribute_value = models.ManyToManyField(
    #     AttributeValue,
    #     verbose_name="attribute value product line",
    #     through="ProductLineAttributeValue",
    #     related_name="product_line_attribute_value",
    #     null=True,
    # )
    created_at = models.DateTimeField(
        _("product created at"), auto_now_add=True, editable=False, null=True
    )

    # Queryser Custom
    objects = ActiveQueryset.as_manager()

    class Meta:
        verbose_name = "ProductLine"
        verbose_name_plural = "ProductLines"

    def __str__(self):
        return str(self.price)
        # return f"{self.product.name} - {self.price} - {self.sku}"

    def save(self, *args, **kwargs):
        self.full_clean()
        self.sku = random_code()
        super(ProductLine, self).save(*args, **kwargs)

    def clean(self, exclude=None):
        qs = ProductLine.objects.filter(product=self.product)
        for obj in qs:
            if self.id != obj.id and self.order == obj.order:
                raise ValidationError("Duplicate order value or Object does not exists")


#!ProductLineAttributeValue


class ProductLineAttributeValue(models.Model):
    attr_value = models.ForeignKey(
        AttributeValue,
        verbose_name="product line attribute value",
        on_delete=models.CASCADE,
        related_name="product_attr_value_av",
    )

    product_line = models.ForeignKey(
        ProductLine,
        verbose_name="product line",
        on_delete=models.CASCADE,
        related_name="product_attr_value_pl",
    )

    class Meta:
        unique_together = ["attr_value", "product_line"]

    def clean(self):
        qs = ProductLineAttributeValue.objects.filter(
            Q(attr_value=self.attr_value) | Q(product_line=self.product_line)
        ).exists()

        if not qs:
            iqs = Attribute.objects.filter(
                attribute_value__product_attr_value_av=self.product_line
            ).values_list(
                "pk", flat=True
            )  # return value list instead of dictionary
            print("Bunedi iqs ", iqs)

            if self.attr_value.attribute.id not in iqs:
                raise ValidationError("Duplicate attribute exists")

    def save(self, *args, **kwargs):
        self.full_clean()
        return super(ProductLineAttributeValue, self).save(*args, **kwargs)


#!ProductImage
class ProductImage(models.Model):
    name = models.CharField(_("product image name"), max_length=100)
    alternative_text = models.CharField(_("alternative text"), max_length=100)
    product_image_url = models.ImageField(
        _("product image url"), upload_to="image/", default="test.png"
    )
    productline = models.ForeignKey(
        ProductLine,
        verbose_name="product line",
        on_delete=models.CASCADE,
        related_name="product_image",
    )
    order = OrderField(
        unique_for_field="productline",
        verbose_name="productline image order",
        blank=True,
    )

    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"

    def __str__(self):
        return str(self.order)

    def clean(self, exclude=None):
        qs = ProductImage.objects.filter(productline=self.productline)
        for obj in qs:
            if self.id != obj.id and self.order == obj.order:
                raise ValidationError("Duplicate order value or Object does not exists")

    def save(self, *args, **kwargs):
        try:
            super(ProductImage, self).save(*args, **kwargs)
        except Exception as e:
            self.full_cean()


#!ProductType
class ProductType(models.Model):
    name = models.CharField(_("product type name"), max_length=100)
    attribute = models.ManyToManyField(
        Attribute, through="ProductTypeAttribute", related_name="product_type_attribute"
    )

    class Meta:
        verbose_name = "Product Type"
        verbose_name_plural = "Product Types"

    def __str__(self):
        return str(self.name)


#!ProductTypeAttribute
class ProductTypeAttribute(models.Model):
    product_type = models.ForeignKey(
        ProductType,
        verbose_name="product type",
        on_delete=models.CASCADE,
        related_name="product_type_attribute_pt",
    )
    attribute = models.ForeignKey(
        Attribute,
        verbose_name="product type attribute",
        on_delete=models.CASCADE,
        related_name="product_type_attribute_a",
    )

    class Meta:
        verbose_name = "Product Type Attribute"
        verbose_name_plural = "Product Type Attributes"
        unique_together = ("product_type", "attribute")

    def __str__(self):
        return f"{self.product_type.name}---{self.attribute.name}"
