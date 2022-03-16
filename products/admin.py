from django.contrib import admin

# Register your models here.
from products.models import Product, Brand

admin.site.register(Brand)
admin.site.register(Product)
