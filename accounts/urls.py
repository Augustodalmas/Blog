# urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import logout_view
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),
]
