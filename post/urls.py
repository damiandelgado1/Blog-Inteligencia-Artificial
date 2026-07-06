from django.contrib import admin
from django.urls import path
from .views import ListBlog, DetailBlog, CreateBlog, DeleteBlog


app_name = "post"

urlpatterns = [
    path('list/', ListBlog.as_view(), name="list_blog"),
    path('detail/<int:pk>/', DetailBlog.as_view(), name="detail_blog"),
    path('create/', CreateBlog.as_view(), name="create_blog"),
    path('delete/<int:pk>/', DeleteBlog.as_view(), name="delete_blog"),
    path('admin/', admin.site.urls),
]