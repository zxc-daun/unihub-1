from django.contrib.auth.models import Group
from django.views import View

from unihub.models import ClubCategory


class DataMixins(View):
    def get_menu(self, exclude=None):
        if exclude is None:
            exclude = []
        menu = [{"title": "Home", "url_name": "home"},
                {"title": "About", "url_name": "about"},
                {"title": "Login", "url_name": "login"},
                {"title": "Register", "url_name": "register"}]
        return [item for item in menu if item["url_name"] not in exclude]

    def get_club_categories(self):
        return ClubCategory.objects.all()

    def get_context_data(self, menu_exclude=None, **kwargs):
        if menu_exclude is None:
            menu_exclude = []
        context = {}
        context['menu'] = self.get_menu(exclude=menu_exclude)
        context['cats'] = self.get_club_categories()
        context.update(kwargs)
        return context



def is_club_admin(user):
    club_admin_group = Group.objects.get(name="club_admin")
    return club_admin_group in user.groups.all()


