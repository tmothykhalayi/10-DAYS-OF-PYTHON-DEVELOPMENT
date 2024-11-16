from django.test import TestCase

# Create your tests here.
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # Fetch the post by its ID
    return render(request, 'post_detail.html', {'post': post})
