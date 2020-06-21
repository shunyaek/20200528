from django.db import models
from django.db.models import Sum
from django.urls import reverse
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(blank=True, null=True, max_length=256)

    def __str__(self):
        return self.title


class ProductImage(models.Model):
    title = models.CharField(blank=True, null=True, max_length=256)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(blank=False, max_length=128, null=True)
    description = models.TextField(blank=True, max_length=None, null=True)
    category = models.ManyToManyField(Category)
    price = models.DecimalField(blank=False, max_digits=10, decimal_places=2, null=True)
    images = models.ManyToManyField(ProductImage)
    discount_availability = models.BooleanField(blank=True, default=False, null=True)
    discount = models.IntegerField(blank=True, null=True)
    availability = models.BooleanField(blank=False, default=True, null=True)
    featured = models.BooleanField(blank=False, default=False, null=True)
    product_added_on = models.DateTimeField(auto_now_add=True, null=True)
    # slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("shop:read-product", kwargs={"id": self.id})

    def get_price(self):
        if self.discount_availability:
            final_price = self.price - ((self.discount / 100.00) * self.price)
        else:
            final_price = self.price
        return final_price

    def get_total_number_of_products(self):
        return self.objects.count()

    def get_availability(self):
        if self.availability:
            return "In stock"
        else:
            return "Out of stock"


class Order(models.Model):
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    order_date = models.DateTimeField(auto_now_add=True, null=True)
