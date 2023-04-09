from django.contrib.auth.models import Group


def is_club_admin(user):
    club_admin_group = Group.objects.get(name="club_admin")
    return club_admin_group in user.groups.all()
