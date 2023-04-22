import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect, JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, DetailView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from accounts import admin
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
from django.views.generic import ListView


class HomeView(View):
    def get(self, request):
        menu = [{"title": "Home", "url_name": "home"}, {"title": "About", "url_name": "about"},
                ]
        cats = ClubCategory.objects.all()

        context = {
            'menu': menu,
            'cats': cats,
        }
        return render(request, 'unihub/home.html', context)


class ClubDetailView(View):
    def get(self, request, slug):
        menu = [{"title": "Home", "url_name": "home"}, {"title": "About", "url_name": "about"},
                {"title": "Login", "url_name": "login"}, {"title": "Register", "url_name": "register"}
                ]
        club = Club.objects.get(slug=slug)
        context = {
            'menu': menu,
            'club': club,
            'events': club.clubevent_set.all(),
        }
        return render(request, 'unihub/club_detail.html', context)


class CustomHandler404View(View):
    def get(self, request, exception):
        menu = [{"title": "Home", "url_name": "home"}, {"title": "About", "url_name": "about"},
                {"title": "Add", "url_name": "add"}]
        context = {
            'menu': menu,
        }
        return render(request, "unihub/404.html", context)


class CustomHandler500View(View):
    def get(self, request):
        menu = [{"title": "Home", "url_name": "home"}, {"title": "About", "url_name": "about"},
                {"title": "Add", "url_name": "add"}]
        context = {
            'menu': menu,
        }
        return render(request, "unihub/500.html", context)


class CustomHandler403View(View):
    def get(self, request, exception):
        menu = [{"title": "Home", "url_name": "home"}, {"title": "About", "url_name": "about"},
                {"title": "Login", "url_name": "login"}, {"title": "Register", "url_name": "register"}]
        context = {
            'menu': menu,
        }
        return render(request, "unihub/403.html", context)


class CustomHandler400View(View):
    def get(self, request, exception):
        menu = [{"title": "Home", "url_name": "home"}, {"title": "About", "url_name": "about"},
                {"title": "Login", "url_name": "login"}, {"title": "Register", "url_name": "register"}]
        context = {
            'menu': menu,
        }
        return render(request, "unihub/400.html", context)


class LoginView(View):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        menu = [{"title": "Home", "url_name": "home"}, {"title": "About", "url_name": "about"},
                {"title": "Register", "url_name": "register"}]
        form = LoginForm()
        context = self.get_context_data()
        context['form'] = form
        context['menu'] = menu
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
                token, _ = Token.objects.get_or_create(user=user)
                request.session['token'] = token.key
                login(request, user)
                if user.groups.filter(name='club_admin').exists():
                    return HttpResponseRedirect(reverse('club_admin_dashboard'))
                else:
                    return HttpResponseRedirect(reverse('user-dashboard'))
            else:
                messages.error(request, "Your username and password didn't match. Please try again.")
            print(request.headers.get('Authorization'))

        context = self.get_context_data()
        context['form'] = form
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        menu = [{"title": "Home", "url_name": "home"}, {"title": "About", "url_name": "about"},
                {"title": "Login", "url_name": "login"}]
        context = {
            'menu': menu,
        }
        return context


class RegisterView(View):
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        context = self.get_context_data()
        context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            is_admin = form.cleaned_data.get("is_admin")
            if is_admin:
                club_admin_group = Group.objects.get(name="club_admin")
                club_admin_group.user_set.add(user)

            user = authenticate(request, username=user.username, password=form.cleaned_data.get("password1"))
            login(request, user)
            messages.success(request, "Registration successful!")

            return redirect('login')
        else:
            messages.error(request, "Error in registration, please check the details.")
        return render(request, 'register.html', {'form': form})

    def get_context_data(self, **kwargs):
        context = {'nav_links': [
            {'name': 'Home', 'url': reverse('home')},
            {'name': 'About', 'url': reverse('about')},
            {'name': 'Login', 'url': reverse('login')},
        ]}
        return context


class LogoutView(View):
    def post(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))


class AboutView(View):
    def get(self, request):
        menu = [{"title": "Home", "url_name": "home"}, {"title": "Login", "url_name": "login"},
                {"title": "Register", "url_name": "register"}]

        context = {
            'menu': menu,
        }
        return render(request, 'about.html', context)


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
class UserDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "unihub/user-dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_user'] = self.request.user
        context['clubs'] = Club.objects.all()
        followed_clubs = ClubMember.objects.filter(user=self.request.user)
        context['followed_clubs'] = followed_clubs
        context['followed_club_ids'] = [club_member.club.id for club_member in followed_clubs]
        return context


class ClubAdminDashboardView(View):
    template_name = 'club_admin_dash/club_admin_dashboard.html'
    context_object_name = 'clubs'

    def get(self, request, *args, **kwargs):
        clubs = Club.objects.filter(creator=request.user)
        club = clubs.first()

        clubs_count = 0
        followers_count = 0
        events_count = 0

        if clubs.exists():
            clubs_count = clubs.count()
            followers_count = ClubMember.objects.filter(club__in=clubs).count()
            events_count = ClubEvent.objects.filter(club__in=clubs).count()

        context = {
            'clubs': clubs,
            'clubs_count': clubs_count,
            'followers_count': followers_count,
            'events_count': events_count,
            'club_slug': club.slug if club else None,
            'events': ClubEvent.objects.filter(club__in=clubs),
        }
        return render(request, self.template_name, context)

    def get_queryset(self):
        return Club.objects.filter(creator=self.request.user.username)


class CreateClubView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'club_admin_dash/create_club.html')


class ClubCategoryViewSet(viewsets.ModelViewSet):
    queryset = ClubCategory.objects.all()
    serializer_class = ClubCategorySerializer


class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        image = self.request.FILES['image']
        constitution = self.request.FILES['constitution']

        image_path = default_storage.save(f"club_images/{image.name}", image)
        constitution_path = default_storage.save(f"club_constitutions/{constitution.name}", constitution)
        category = ClubCategory.objects.get(pk=self.request.data['category'])

        serializer.save(
            image=image_path,
            constitution=constitution_path,
            creator=self.request.user,
            category=category
        )

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        print("Destroy method called")
        instance = self.get_object()
        print(f"Deleting club with ID: {instance.pk}")
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


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


class ClubListAPIView(generics.ListAPIView):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer


class LogoutAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class ClubFollowView(View):
    def post(self, request, *args, **kwargs):
        user = request.user
        club_id = request.POST.get('club_id')
        club = Club.objects.get(id=club_id)

        if user.is_authenticated:
            club_member, created = ClubMember.objects.get_or_create(user=user, club=club)

            if created:
                response = {'status': 'followed'}
            else:
                club_member.delete()
                response = {'status': 'unfollowed'}

            return JsonResponse(response)
        else:
            return JsonResponse({'status': 'error', 'message': 'User is not authenticated'})


class ShowClubFollowersView(UserPassesTestMixin, ListView):
    model = ClubMember
    template_name = 'club_admin_dash/show_followers.html'
    context_object_name = 'followers'

    def get_queryset(self):
        club = Club.objects.get(slug=self.kwargs['slug'])
        return ClubMember.objects.filter(club=club)

    def test_func(self):
        club = Club.objects.get(slug=self.kwargs['slug'])
        return self.request.user == club.creator


class ClubInfoView(DetailView):
    model = Club
    template_name = 'club_info.html'
    context_object_name = 'club'
    slug_url_kwarg = 'slug'


class EditProfileView(LoginRequiredMixin, View):
    template_name = 'unihub/edit_profile.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        # Get user info from the form
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        user_image = request.FILES.get('user_image', None)

        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        user.save()

        profile, _ = UserProfile.objects.get_or_create(user=user)
        if user_image:
            profile.user_image = user_image
            profile.save()

        messages.success(request, 'Profile updated successfully')
        return redirect('edit_profile')


class CreateEventView(LoginRequiredMixin, View):
    template_name = 'club_admin_dash/create_event.html'

    def get(self, request):
        club_id = request.GET.get('club', '')
        club = None
        if club_id:
            try:
                club = Club.objects.get(id=club_id)
            except Club.DoesNotExist:
                messages.error(request, 'Club not found')
                club = None

        clubs = Club.objects.filter(creator=request.user)

        context = {'club': club, 'clubs': clubs}
        return render(request, self.template_name, context)

    def post(self, request):
        title = request.POST.get('title')
        description = request.POST.get('description')
        start_time = request.POST.get('start_date')
        end_time = request.POST.get('end_date')
        club_id = request.POST.get('club')
        location = request.POST.get('location')

        if club_id:
            try:
                club = Club.objects.get(id=club_id)
            except Club.DoesNotExist:
                return JsonResponse({'status': 'error', 'message': 'Club not found'})

            if request.user == club.creator:
                club_event = ClubEvent.objects.create(
                    name=title,
                    description=description,
                    start_time=start_time,
                    end_time=end_time,
                    club=club,
                    location=location,
                    creator=request.user
                )
                club_event.save()
                print('Event created successfully')
                return redirect('club_admin_dashboard')
            else:
                return render(request, self.template_name, {'error': 'You are not the creator of this club'})

        return JsonResponse({'status': 'error', 'message': 'Invalid club ID'})


class ClubEventListView(ListView):
    model = ClubEvent
    template_name = 'club_admin_dash/club_event_list.html'
    context_object_name = 'events'

    def get(self, request, *args, **kwargs):
        events = ClubEvent.objects.filter(club__slug=self.kwargs['slug'])
        context = {'events': events, 'club': self.kwargs['slug']}
        return render(request, self.template_name, context)

    def get_queryset(self):
        club = Club.objects.get(slug=self.kwargs['slug'])
        return ClubEvent.objects.filter(club=club)


@csrf_exempt
def update_event(request, event_id):
    if request.method == 'PUT':
        event = get_object_or_404(ClubEvent, id=event_id)
        data = json.loads(request.body)

        event.name = data.get('name', event.name)
        event.description = data.get('description', event.description)
        event.location = data.get('location', event.location)
        event.save()

        return JsonResponse({'status': 'success', 'message': 'Event updated'})


@csrf_exempt
def delete_event(request, event_id):
    if request.method == 'DELETE':
        event = get_object_or_404(ClubEvent, id=event_id)
        event.delete()

        return JsonResponse({'status': 'success', 'message': 'Event deleted'})


@csrf_exempt
def complete_event(request, event_id):
    if request.method == 'POST':
        event = get_object_or_404(ClubEvent, id=event_id)
        event.completed = True
        event.save()

        return JsonResponse({'status': 'success', 'message': 'Event marked as complete'})


class CategoryView(TemplateView):
    template_name = 'unihub/category_template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs['category_slug']
        category = ClubCategory.objects.get(slug=category_slug)
        context['category'] = category
        menu = [{"title": "Home", "url_name": "home"}, {"title": "Login", "url_name": "login"},
                {"title": "Register", "url_name": "register"}, {"title": "About", "url_name": "about"}]
        context['menu'] = menu
        return context


