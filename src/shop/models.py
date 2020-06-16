from django.db import models
from django.urls import reverse


class Product(models.Model):

    title = models.CharField(blank=False, max_length=128)
    summary = models.TextField(blank=True, max_length=256)
    description = models.TextField(blank=True, max_length=None)
    price = models.DecimalField(blank=False, max_digits=10, decimal_places=2)
    discount_availability = models.BooleanField(blank=True, default=False)
    discount = models.DecimalField(
        blank=True, null=True, max_digits=5, decimal_places=2
    )
    availability_status = models.BooleanField(blank=False, default=True)
    featured = models.BooleanField(blank=False, default=False)
    product_added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('shop:read-product', kwargs={'id': self.id})

    def get_price(self):
        if self.discount_availability:
            final_price = self.price - ((self.discount / 100.00) * self.price)
        else:
            final_price = self.price
        return final_price
