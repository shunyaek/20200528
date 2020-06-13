from django.db import models


class Author(models.Model):
    name = models.CharField()


class Post(models.Model):
    title = models.CharField(blank=False, max_length=128)
    author = models.ForeignKey("Author")
