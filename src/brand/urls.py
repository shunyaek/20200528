from django.urls import path

from .views import (
    sign_up_view,
    sign_in_view,
)

app_name = "brand"
urlpatterns = [
    path("signup/", sign_up_view, name="sign_up"),
    path("signin/", sign_in_view, name="sign_in"),
]