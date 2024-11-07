from django.db import models

# Create your models here.
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)  # Title of the post
    content = models.TextField()  # Content of the post
    author = models.CharField(max_length=100)  # Author of the post
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-set when the post is created
    updated_at = models.DateTimeField(auto_now=True)  # Auto-set when the post is updated

    def __str__(self):
        return self.title  # When we print, show the title of the post

