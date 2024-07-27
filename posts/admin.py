from django.contrib import admin
from posts.models import Comentario, Post

class adminPost(admin.ModelAdmin):
    list_display = ("titulo",)
    class Meta:
        model = Post
        fields = '__all__'


class adminComentario(admin.ModelAdmin):
    list_display = ("postagem",)


admin.site.register(Post, adminPost)
admin.site.register(Comentario, adminComentario)