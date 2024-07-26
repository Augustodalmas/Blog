from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from posts.models import Post, Comentario
from posts.form import commentform, postform
from django.urls import reverse

class createPost(CreateView):
    model = Post
    form_class = postform
    template_name = 'criar_postagem.html'
    context_object_name = 'createpostagem'
    success_url = '/lista'

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.publicado = False
        return super().form_valid(form)


class listPost(ListView):
    model = Post
    template_name = 'pagina_inicial.html'
    context_object_name = "postagem"
    paginate_by = '5'

    def get_queryset(self):
        return Post.objects.order_by('-id')


class detailPost(DetailView):
    model = Post
    template_name = 'detalhe.html'
    context_object_name = "comentarios"
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['postagem'] = Post.objects.get(pk=self.kwargs['pk'])
        context['comentarios'] = self.object.comentarios.all()  # Supondo relação de ForeignKey entre Noticia e Comentario
        return context
    

class createComent(CreateView):
    model = Comentario
    form_class = commentform
    template_name = 'criar_comentario.html'
    context_object_name = 'comentario'
    
    def form_valid(self, form):
        # Associa o comentário à postagem correta antes de salvar
        form.instance.postagem = Post.objects.get(pk=self.kwargs['pk'])
        form.instance.autor = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('detalhaPostagem', kwargs={'pk': self.object.postagem.pk})

