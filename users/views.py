from django.shortcuts import render, redirect

from users.forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from shop.settings import LOGIN_REDIRECT_URL
from .forms import AuthForm
from django.views.generic import DetailView
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'users/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        return render(request, 'users/register.html', {'user_form': user_form})
        

def log_in(request):
    form = AuthForm(request, data=request.POST or None)

    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            url = request.GET.get('next', LOGIN_REDIRECT_URL)
            return redirect(url)

    return render(request, 'users/login.html', {'form': form})


def log_out(request):
    logout(request)
    url = reverse('products:index')
    return redirect(url)


class UserDetailView(DetailView):
    model = User
    template_name = 'users/user-info.html'