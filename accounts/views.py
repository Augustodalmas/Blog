# views.py

from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.shortcuts import redirect
from accounts.forms import CustomUserCreationForm

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('user-list')  # redireciona para a página inicial após o registro

    def form_valid(self, form):
        # Após o registro bem-sucedido, faz o login automaticamente
        user = form.save()
        auth_login(self.request, user)
        return super().form_valid(form)
    

def logout_view(request):
    logout(request)
    return redirect('listaPostagem')
