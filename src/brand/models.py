from django.db import models


class WidgetGrid(models.Model):
    pass


class WidgetBanner(models.Model):
    title = models.CharField(blank=False, max_length=32)
    sub_title = models.TextField(blank=True, max_length=128)
    background = models.ImageField()
    enabled = models.BooleanField(default=True)


class WidgetInformational(models.Model):
    heading = models.CharField(blank=False, max_length=32)
    content = models.TextField(blank=True, max_length=128)
    image = models.ImageField()
    # form =
    enabled = models.BooleanField(default=True)


class Page(models.Model):
    title = models.CharField(blank=False, null=False, max_length=16)
