from django.urls import path

from blog.views import (
    blog_view,
    create_post_view,
    read_post_view,
    update_post_view,
    delete_post_view,
)

app_name = "blog"
urlpatterns = [
    path("", blog_view, name="blog_home"),
    path("create/", create_post_view, name="create_post"),
    path("<int:pk>/", read_post_view, name="read_post"),
    path("<int:pk>/update/", update_post_view, name="update_post"),
    path("<int:pk>/delete/", delete_post_view, name="delete_post"),
]
