from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# from ckeditor.fields import RichTextField

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    criado_em = models.DateField(auto_now=True)
    atualizado_em = models.DateField(auto_now=True)
    publicado = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
    

    def get_absolute_url(self):
        return f"/blog/{self.slug}/"
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)


class Comentario(models.Model):
    postagem = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comentarios")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    criado_em = models.DateField(auto_now=True)

    def __str__(self):
        return f"comentario de {self.autor} em {self.postagem}"
