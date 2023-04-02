from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User

class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        print("EmailBackend: authenticate called")
        try:
            user = User.objects.get(email=username)
            print("User found:", user)
            if user.check_password(password):
                print("Password matched")
                return user
            else:
                print("Password mismatch")
        except User.DoesNotExist:
            print("User not found")
            return None

    def get_user(self, user_id):
        print("EmailBackend: get_user called")
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
