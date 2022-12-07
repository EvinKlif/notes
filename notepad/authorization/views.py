from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from authorization.forms import RegisterUserForm, LoginUserForm


class RegisterUser(CreateView):
    """User registration."""
    form_class = RegisterUserForm
    template_name = 'authorization/register.html'

    def form_valid(self, form):
        user = form.save()
        return redirect('login')


class LoginUser(LoginView):
    """User login."""
    form_class = LoginUserForm
    template_name = 'authorization/login.html'

    def get_success_url(self):
        return reverse_lazy('notes')


def logout_user(request):
    """User logout."""
    logout(request)
    return redirect('login')


def home_view(request):
    return render(request, 'authorization/main.html')
