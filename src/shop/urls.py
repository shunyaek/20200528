from django.urls import path

from shop.views import (
    shop_view,
    product_view,
    create_product_view,
    update_product_view,
    checkout_view,
    create_payment_intent_view,
    payment_complete_view,
)

app_name = "shop"
urlpatterns = [
    path("", shop_view, name="shop_home"),
    path("checkout/", checkout_view, name="checkout"),
    path("create-payment-intent", create_payment_intent_view, name="create-payment-intent"),
    path("payment-complete", payment_complete_view, name="payment-complete"),
    path("product/", product_view, name="read-product"),
    path("create/", create_product_view, name="create-product"),
    # path('<int:id>/', read_product_view, name='read-product'),
    path("<int:id>/update/", update_product_view, name="update-product"),
    # path('<int:id>/delete/', delete_product_view, name='delete-product'),
]
