from django.urls import path

from shop.views import (
    shop_view,
    create_product_view,
    read_product_view,
    update_product_view,
    delete_product_view,
)

app_name = 'shop'
urlpatterns = [
    path('', shop_view, name='shop-home'),
    path('create/', create_product_view, name='create-product'),
    path('read/', read_product_view, name='read-product'),
    path('update/', update_product_view, name='update-product'),
    path('delete/', delete_product_view, name='delete-product'),
]
