from django.contrib import admin
from . import models as m

# Register your models here.


# *ProductLineInline
class ProductLineInline(admin.TabularInline):
    model = m.ProductLine
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


# ?Default Register Model
admin.site.register(m.ProductLine)
