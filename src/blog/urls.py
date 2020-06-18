from django.urls import path

from blog.views import blog_view, read_post_view

app_name = 'blog'
urlpatterns = [
    path('', blog_view, name='blog_home'),
    # path('create/', create_blog_view, name='create-product'),
    path('post/<int:pk>/', read_post_view, name='read_post'),
    # path('<int:id>/update/', update_blog_view, name='update-product'),
    # path('<int:id>/delete/', delete_product_view, name='delete-product'),
]
