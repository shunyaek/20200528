from django.db import models
from django.conf import settings
from django.urls import reverse


class Author(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_image = models.ImageField(
        upload_to="authors/{}/profile_images/".format(settings.AUTH_USER_MODEL),
        default='{% static "default_images/user-solid.svg" %}',
    )

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(blank=False, max_length=128)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to="posts/images/")

    def get_absolute_url(self):
        return reverse("blog:read_post", kwargs={"id": self.id})
