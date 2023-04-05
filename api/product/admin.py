# Django Functions and Modules
from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe


# Models,Forms and Serializers class
from . import models as m


# Register your models here.


# ?EditLinkInline
class EditLinkInline(object):
    def edit(self, instance):
        url = reverse(
            f"admin:{instance._meta.app_label}_{instance._meta.model_name}_change",
            args=[instance.pk],
        )
        if instance.pk:
            link = mark_safe(
                '<a href="{u}" style="color:#30336b;font-weight:bold">Edit</a>'.format(
                    u=url
                )
            )
            return link
        else:
            return ""


# *ProductLineInline
class ProductLineInline(EditLinkInline, admin.TabularInline):
    model = m.ProductLine
    readonly_fields = ("edit",)
    extra = 1


# *ProductImageInline
class ProductImageInline(admin.TabularInline):
    model = m.ProductImage
    exclude = ["name"]
    extra = 1


#################################################################################################

#!CategoryAdmin
@admin.register(m.Category)
class CategoryAdmin(admin.ModelAdmin):
    model = m.Category


#!BrandAdmin
@admin.register(m.Brand)
class BrandAdmin(admin.ModelAdmin):
    model = m.Brand


#!ProductAdmin
@admin.register(m.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductLineInline]
    list_display = ["name", "is_digital", "is_active"]


#!ProductLineAdmin
@admin.register(m.ProductLine)
class ProductLineAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]


admin.site.register(m.Attribute)
admin.site.register(m.AttributeValue)
admin.site.register(m.ProductLineAttributeValue)
