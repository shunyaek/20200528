from django.urls import path

from shop.views import (
    shop_view,
    create_product_view,
    update_product_view,
)

app_name = 'shop'
urlpatterns = [
    path('', shop_view, name='shop_home'),
    path('create/', create_product_view, name='create-product'),
    # path('<int:id>/', read_product_view, name='read-product'),
    path('<int:id>/update/', update_product_view, name='update-product'),
    # path('<int:id>/delete/', delete_product_view, name='delete-product'),
]
