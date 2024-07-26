from django import forms
from posts.models import Comentario, Post

class commentform(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ('comentario',)
        widgets = {
            'conteudo': forms.Textarea(attrs={
            'class': 'form-control',
            'id': 'Textarea1',
            'rows': 17,
            'placeholder': 'Digite o conteúdo aqui...'
            })
        }

class postform(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['titulo', 'conteudo']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'Input1',
                'placeholder': 'Digite seu titulo aqui...'
            }),
            'conteudo': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'Textarea1',
                'rows': 17,
                'placeholder': 'Digite o conteúdo aqui...'
            }),
        }
