from django.contrib import admin
from .models import Product, ProductQuantity, ProductImage

admin.site.register(Product)
admin.site.register(ProductQuantity)
admin.site.register(ProductImage)
