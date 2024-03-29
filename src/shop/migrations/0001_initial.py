# Generated by Django 3.0.7 on 2020-06-12 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=128)),
                ("summary", models.TextField(blank=True, max_length=256)),
                ("description", models.TextField(blank=True)),
                ("price", models.DecimalField(decimal_places=3, max_digits=10)),
                (
                    "discount_availability",
                    models.BooleanField(blank=True, default=False),
                ),
                (
                    "discount",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                ("availability_status", models.BooleanField(default=True)),
                ("featured", models.BooleanField(default=False)),
                ("product_added_on", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
