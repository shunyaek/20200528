from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(blank=False, null=True, max_length=128)
    publication_date = models.DateTimeField(auto_now_add=True, null=True)
    content = models.TextField(blank=False, null=True)
    featured = models.BooleanField(default=False, null=True)
    image = models.ImageField(blank=True, null=True, upload_to="posts/images/")

    def get_absolute_url(self):
        return reverse("blog:read_post", kwargs={"id": self.id})
