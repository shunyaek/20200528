from django.db import models


class Page(models.Model):
    title = models.CharField(blank=False, null=False, max_length=16)
