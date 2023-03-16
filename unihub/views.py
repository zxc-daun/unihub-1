from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import View
from django.contrib import messages
from django.views.generic.edit import CreateView, FormView
from .forms import RegisterForm, NewRegisterForm, CustomUserCreationForm, CustomAuthenticationForm
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


def login(request):
    menu = [{"title": "Home", "url_name": "home"}, {"title": "About", "url_name": "about"},
            {"title": "Add", "url_name": "add"}]

    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = CustomAuthenticationForm(request)
    context = {
        'menu': menu,
        'form': form,
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
    form_class = CustomAuthenticationForm
    template_name = 'unihub/login.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse('user_profile')

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'unihub/login.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return reverse('user_profile')

    def form_valid(self, form):
        # Authenticate user
        username_or_email = form.cleaned_data['username_or_email']
        password = form.cleaned_data['password']
        user = authenticate(
            self.request,
            username_or_email=username_or_email,
            password=password
        )

        # If user is authenticated, log them in and redirect to success URL
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            # If authentication fails, add error to form
            form.add_error('username_or_email', 'Invalid username/email or password')
            return self.form_invalid(form)


class LogoutView(View):
    def get(self, request):
        menu = [{"title": "Home", "url_name": "home"}, {"title": "About", "url_name": "about"},
                {"title": "Add", "url_name": "add"}, {"title": "Login", "url_name": "login"},
                {"title": "Register", "url_name": "register"}]
        context = {
            'menu': menu,
        }
        return render(request, 'unihub/logout.html', context)


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
