from django.shortcuts import render
from post.models import Blog

def blog_site(request):
    posts = Blog.objects.all()
    return render(request, "home/base.html", {"posts": posts})