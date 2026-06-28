from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Blog

# Display all Blog's
class ListBlog(ListView):
    model = Blog
    template_name = ""
    context_object_name = "blogs"


# Show detail content a Blog
class DetailBlog(DetailView):
    model = Blog
    template_name = ""
    context_object_name = "blog"


# Create new Blog in the site
class CreateBlog(CreateView):
    model = Blog
    fields = [
        "name",
        "photo",
        "category",
        "content"
    ]
    template_name = ""
    success_url = reverse_lazy("")


# Delete a Blog in the site
class DeleteBlog(DeleteView):
    model = Blog
    template_name = ""
    success_url = reverse_lazy("")