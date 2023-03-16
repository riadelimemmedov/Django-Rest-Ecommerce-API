from django.contrib import admin
from . import models as m

# Register your models here.


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
    model = m.Product
