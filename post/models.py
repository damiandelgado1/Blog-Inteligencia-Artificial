from django.db import models

# Content of the Blog
class Blog(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nombre del Blog")
    category = models.CharField(max_length=30, verbose_name="Categoria del Blog")
    content = models.TextField(verbose_name="Contenido del Blog")
    created_at = models.DateTimeField(auto_now=True, verbose_name="Fecha del Blog")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "posts"
        verbose_name_plural = "post"