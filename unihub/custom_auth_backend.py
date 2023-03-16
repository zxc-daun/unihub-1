# custom_auth_backend.py

from django.contrib.auth.backends import ModelBackend
from unihub.models import CustomUser


class CustomAuthenticationBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        username_or_email = kwargs.get('username_or_email')
        password = kwargs.get('password')

        # Authenticate user based on your custom user model
        try:
            user = CustomUser.objects.get(username=username_or_email)
        except CustomUser.DoesNotExist:
            return None

        if user.check_password(password):
            return user

        return None
