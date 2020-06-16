from django.db import models
from django.db.models import Sum
from django.urls import reverse
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(blank=False, max_length=128)
    summary = models.TextField(blank=True, max_length=256)
    description = models.TextField(blank=True, max_length=None)
    price = models.DecimalField(blank=False, max_digits=10, decimal_places=2)
    images = models.ManyToManyField(ProductImage)
    discount_availability = models.BooleanField(blank=True, default=False)
    discount = models.DecimalField(
        blank=True, null=True, max_digits=5, decimal_places=2
    )
    availability_status = models.BooleanField(blank=False, default=True)
    featured = models.BooleanField(blank=False, default=False)
    product_added_on = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField()

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


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()


class OrderItem(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)

    def __str__(self):
        return self.user.username

    def get_cart_count(self):
        return self.items.count()

    """ def get_cart_total(self):
        return self.items.all().aggregate(Sum()) """
