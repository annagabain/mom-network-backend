from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # post_image = models.ImageField(
    #     upload_to='images/', default='../pngkey.com-ega-png-2332677_enun3f'
    # )
    post_image = models.ImageField(upload_to='images/', blank=True)

    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return self.owner.username + ' says: ' + self.content
        # return self.content

