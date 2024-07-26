from django.contrib import admin
from django.urls import path
from posts.views import listPost, detailPost, createComent, createPost

urlpatterns = [
    path('lista', listPost.as_view(), name='listaPostagem'),
    path('lista/<int:pk>/', detailPost.as_view(), name='detalhaPostagem'),
    path('lista/<int:pk>/criar-comentario', createComent.as_view(), name='criarComentario'),
    path('lista/criar-postagem', createPost.as_view(), name='criarPostagem'),
]