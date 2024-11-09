from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse  # Import reverse for URL generation

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # Add a method to get the URL for the post's detail view
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
