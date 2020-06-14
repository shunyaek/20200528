from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField()

    def __str__(self):
        return self.user.username



class Post(models.Model):
    title = models.CharField(blank=False, max_length=128)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    summary = models.TextField()
    featured = models.BooleanField(default=False)
    thumbnail = models.ImageField()
