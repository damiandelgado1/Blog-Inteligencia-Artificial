from django.contrib import admin
from django.urls import path, include
from .views import blog_site


urlpatterns = [
    path('', blog_site, name="home"),
    path('post/', include("post.urls", namespace="post")),
    path('admin/', admin.site.urls),
]