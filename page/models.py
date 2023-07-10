from django.db import models
from django.contrib.auth.models import User

class Page(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='page_images/')
    followers = models.ManyToManyField(User, related_name='following_pages')
    posts = models.ManyToManyField('posts.Post', related_name='page')

    def __str__(self):
        return self.title
