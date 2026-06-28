from django.db import models

# Content of the Blog
class Blog(models.Model):
    name = models.CharField(max_length=20, verbose_name="Nombre del Blog")
    photo = models.ImageField(upload_to="", verbose_name="Foto del Blog")
    category = models.CharField(max_length=20, verbose_name="Categoria del Blog")
    content = models.TextField(verbose_name="Contenido del Blog")
    created_at = models.DateTimeField(auto_now=True, verbose_name="Fecha del Blog")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "blogs"
        verbose_name_plural = "blog"