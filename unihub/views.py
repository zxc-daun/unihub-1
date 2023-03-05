from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import View
from django.contrib import messages
from django.views.generic.edit import CreateView, FormView
from .forms import RegisterForm, NewRegisterForm, CustomUserCreationForm, CustomAuthenticationForm
from .models import *


def home(request):
    menu = [{"title": "Home", "url_name": "home"}, {"title": "About", "url_name": "about"},
            {"title": "Add", "url_name": "add"}]
    cats = ClubCategory.objects.all()

    context = {
        'menu': menu,
        'cats': cats,
    }
    return render(request, 'unihub/home.html', context)


# Show club by slug
def club_detail(request, slug):
    menu = [{"title": "Home", "url_name": "home"}, {"title": "About", "url_name": "about"},
            {"title": "Add", "url_name": "add"}]
    club = Club.objects.get(slug=slug)
    context = {
        'menu': menu,
        'club': club,
    }
    return render(request, 'unihub/club_detail.html', context)


def custom_handler404(request, exception):
    menu = [{"title": "Home", "url_name": "home"}, {"title": "About", "url_name": "about"},
            {"title": "Add", "url_name": "add"}]
    context = {
        'menu': menu,
    }
    return render(request, "unihub/404.html", context)  # not found


def custom_handler500(request):
    menu = [{"title": "Home", "url_name": "home"}, {"title": "About", "url_name": "about"},
            {"title": "Add", "url_name": "add"}]
    context = {
        'menu': menu,
    }
    return render(request, "unihub/500.html", context)  # internal server error


def custom_handler403(request, exception):
    menu = [{"title": "Home", "url_name": "home"}, {"title": "About", "url_name": "about"},
            {"title": "Add", "url_name": "add"}]
    context = {
        'menu': menu,
    }
    return render(request, "unihub/403.html", context)  # forbidden


def custom_handler400(request, exception):
    menu = [{"title": "Home", "url_name": "home"}, {"title": "About", "url_name": "about"},
            {"title": "Add", "url_name": "add"}]
    context = {
        'menu': menu,
    }
    return render(request, "unihub/400.html", context)  # bad request


def login(request):
    menu = [{"title": "Home", "url_name": "home"}, {"title": "About", "url_name": "about"},
            {"title": "Add", "url_name": "add"}]
    context = {
        'menu': menu,
    }
    return render(request, 'unihub/login.html', context)


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'unihub/register.html'
    success_url = reverse_lazy('login')

    def get_user_context(self, **kwargs):
        context = {
            'title': kwargs.get('title', ''),
        }
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Registration')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Your account has been created! You can now log in.')
        return response


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'unihub/login.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        email = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(
            self.request,
            email=email,
            password=password
        )
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            form.add_error(None, 'Invalid email or password')
            return super().form_invalid(form)


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'unihub/login.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context


def logout(request):
    menu = [{"title": "Home", "url_name": "home"}, {"title": "About", "url_name": "about"},
            {"title": "Add", "url_name": "add"}, {"title": "Login", "url_name": "login"},
            {"title": "Register", "url_name": "register"}]
    context = {
        'menu': menu,
    }
    return render(request, 'unihub/logout.html', context)


def add(request):
    menu = [{"title": "Home", "url_name": "home"}, {"title": "About", "url_name": "about"},
            {"title": "Add", "url_name": "add"}]
    context = {
        'menu': menu,
    }
    return render(request, 'unihub/add.html', context)


def fetch_clubs(request):
    menu = [{"title": "Home", "url_name": "home"},
            {"title": "About", "url_name": "about"},
            {"title": "Add", "url_name": "add"},
            {"title": "Login", "url_name": "login"},
            {"title": "Register", "url_name": "register"},
            ]

    clubs = Club.objects.all()
    context = {
        'menu': menu,
        'clubs': clubs,
    }
    return render(request, 'unihub/home.html', context)
