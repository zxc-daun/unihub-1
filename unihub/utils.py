from django.contrib.auth.models import Group


def assign_role(user, role_name):
    group = Group.objects.get(name=role_name)
    user_profile = user.userprofile
    user_profile.roles.add(group)
    user_profile.save()
