# Generated by Django 3.0.7 on 2020-06-17 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200617_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='profile_photo',
        ),
        migrations.AddField(
            model_name='author',
            name='profile_image',
            field=models.ImageField(default='{% static "default_images/user-solid.svg" %}', upload_to='authors/auth.User/profile_images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='posts/images/'),
        ),
    ]
