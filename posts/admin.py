from django.contrib import admin
from posts.models import Comentario, Post
from ckeditor.widgets import CKEditorWidget

class adminPost(admin.ModelAdmin):
    list_display = ("titulo",)
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'conteudo': CKEditorWidget(),
        }



class adminComentario(admin.ModelAdmin):
    list_display = ("postagem",)


admin.site.register(Post, adminPost)
admin.site.register(Comentario, adminComentario)