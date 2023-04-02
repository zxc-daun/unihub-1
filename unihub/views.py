from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_exempt

from .forms import LoginForm, RegistrationForm

from .models import *


class HomeView(View):
    def get(self, request):
        menu = [{"title": "Home", "url_name": "home"}, {"title": "About", "url_name": "about"},
                {"title": "Add", "url_name": "add"}]
        cats = ClubCategory.objects.all()

        context = {
            'menu': menu,
            'cats': cats,
        }
        return render(request, 'unihub/home.html', context)


class ClubDetailView(View):
    def get(self, request, slug):
        menu = [{"title": "Home", "url_name": "home"}, {"title": "About", "url_name": "about"},
                {"title": "Add", "url_name": "add"}]
        club = Club.objects.get(slug=slug)
        context = {
            'menu': menu,
            'club': club,
        }
        return render(request, 'unihub/club_detail.html', context)


class CustomHandler404View(View):
    def get(self, request, exception):
        menu = [{"title": "Home", "url_name": "home"}, {"title": "About", "url_name": "about"},
                {"title": "Add", "url_name": "add"}]
        context = {
            'menu': menu,
        }
        return render(request, "unihub/404.html", context)  # not found


class CustomHandler500View(View):
    def get(self, request):
        menu = [{"title": "Home", "url_name": "home"}, {"title": "About", "url_name": "about"},
                {"title": "Add", "url_name": "add"}]
        context = {
            'menu': menu,
        }
        return render(request, "unihub/500.html", context)  # internal server error


class CustomHandler403View(View):
    def get(self, request, exception):
        menu = [{"title": "Home", "url_name": "home"}, {"title": "About", "url_name": "about"},
                {"title": "Add", "url_name": "add"}]
        context = {
            'menu': menu,
        }
        return render(request, "unihub/403.html", context)  # forbidden


class CustomHandler400View(View):
    def get(self, request, exception):
        menu = [{"title": "Home", "url_name": "home"}, {"title": "About", "url_name": "about"},
                {"title": "Add", "url_name": "add"}]
        context = {
            'menu': menu,
        }
        return render(request, "unihub/400.html", context)  # bad request


@method_decorator(login_required, name='dispatch')
class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'unihub/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            print("Form Data:", form.cleaned_data)
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            print("Authenticated User:", user)
            if user is not None:
                login(request, user)
                print("User:", user)
                print("Request User:", request.user)
                return redirect(reverse_lazy('user-dashboard'))
        return render(request, 'unihub/login.html', {'form': form})


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        return render(request, 'unihub/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, 'unihub/register.html', {'form': form})


class LogoutView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        logout(request)  # Log out the user
        return render(request, 'unihub/login.html')


class AddView(View):
    def get(self, request):
        menu = [{"title": "Home", "url_name": "home"}, {"title": "About", "url_name": "about"},
                {"title": "Add", "url_name": "add"}]
        context = {
            'menu': menu,
        }
        return render(request, 'unihub/add.html', context)


class FetchClubsView(View):
    def get(self, request):
        menu = [{"title": "Home", "url_name": "home"},
                {"title": "About", "url_name": "about"},
                {"title": "Add", "url_name": "add"},
                {"title": "Login", "url_name": "login"},
                {"title": "Register", "url_name": "register"}]

        clubs = Club.objects.all()
        context = {
            'menu': menu,
            'clubs': clubs,
        }
        return render(request, 'unihub/home.html', context)


class UserDashboardView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, 'unihub/user-dashboard.html')
