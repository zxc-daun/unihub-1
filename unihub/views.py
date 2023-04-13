from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.cache import never_cache

from .forms import LoginForm, RegistrationForm
from django.contrib import messages
from rest_framework import viewsets, generics
from .serializers import *
from .models import *
from django.core.files.storage import default_storage
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

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


class LoginView(View):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        context = self.get_context_data()
        context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                if user.groups.filter(name='club_admin').exists():
                    # The user is a club admin, redirect to club_admin_dashboard
                    return redirect(reverse('club_admin_dashboard'))
                else:
                    # The user is not a club admin, redirect to user_dashboard
                    return redirect(reverse('user_dashboard'))
            else:
                messages.error(request, "Your username and password didn't match. Please try again.")

            # Print the token here
            print(request.headers.get('Authorization'))

        context = self.get_context_data()
        context['form'] = form
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = {}
        return context


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            is_admin = form.cleaned_data.get("is_admin")
            if is_admin:
                club_admin_group = Group.objects.get(name="club_admin")
                club_admin_group.user_set.add(user)

            # Authenticate the user to set the backend attribute
            user = authenticate(request, username=user.username, password=form.cleaned_data.get("password1"))
            login(request, user)
            messages.success(request, "Registration successful!")

            if is_admin:
                return redirect(reverse('club_admin_dashboard'))
            else:
                return redirect(reverse('user-dashboard'))
        else:
            messages.error(request, "Error in registration, please check the details.")
        return render(request, 'register.html', {'form': form})


class LogoutView(View):
    def post(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))


class AboutView(View):
    def get(self, request):
        menu = [{"title": "Home", "url_name": "home"}, {"title": "About", "url_name": "about"},
                {"title": "Add", "url_name": "add"}]
        context = {
            'menu': menu,
        }
        return render(request, 'unihub/about.html', context)


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


@method_decorator(login_required, name='dispatch')
@method_decorator(never_cache, name='dispatch')
class UserDashboardView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, 'unihub/user-dashboard.html')


class ClubAdminDashboardView(View):
    template_name = 'club_admin_dash/club_admin_dashboard.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)


class CreateClubView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'club_admin_dash/create_club.html')


class ClubCategoryViewSet(viewsets.ModelViewSet):
    queryset = ClubCategory.objects.all()
    serializer_class = ClubCategorySerializer


class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        image = self.request.FILES['image']
        constitution = self.request.FILES['constitution']

        image_path = default_storage.save(f"club_images/{image.name}", image)
        constitution_path = default_storage.save(f"club_constitutions/{constitution.name}", constitution)

        serializer.save(
            image=image_path,
            constitution=constitution_path,
            creator=self.request.user
        )


class ClubEventViewSet(viewsets.ModelViewSet):
    queryset = ClubEvent.objects.all()
    serializer_class = ClubEventSerializer


class ClubMemberViewSet(viewsets.ModelViewSet):
    queryset = ClubMember.objects.all()
    serializer_class = ClubMemberSerializer


class ClubMeetingViewSet(viewsets.ModelViewSet):
    queryset = ClubMeeting.objects.all()
    serializer_class = ClubMeetingSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserClubViewSet(viewsets.ModelViewSet):
    queryset = UserClub.objects.all()
    serializer_class = UserClubSerializer


class LoginApiView(APIView):

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)
        except User.DoesNotExist:
            user = None

        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)


class ClubListAPIView(generics.ListAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer




