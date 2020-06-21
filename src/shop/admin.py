from django.contrib import admin
from .models import Product, Customer, ProductImage, Order, Category

admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(Product)
admin.site.register(Order)
