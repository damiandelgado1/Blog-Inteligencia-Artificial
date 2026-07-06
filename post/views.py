from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Blog


# Display all Blog's
class ListBlog(ListView):
    model = Blog
    template_name = "blog/list_blog.html"
    context_object_name = "posts"


# Show detail content a Blog
class DetailBlog(DetailView):
    model = Blog
    template_name = "blog/detail_blog.html"
    context_object_name = "post"


# Create new Blog in the site
class CreateBlog(CreateView):
    model = Blog
    fields = [
        "name",
        "category",
        "content"
    ]
    template_name = "blog/create_blog.html"
    success_url = reverse_lazy("home")


# Delete a Blog in the site
class DeleteBlog(DeleteView):
    model = Blog
    template_name = "blog/delete_blog.html"
    success_url = reverse_lazy("home")