from django.contrib.auth.models import User


class SillyAuthBackend(object):
    def authenticate(self, username=None, password=None):
        user, created = User.objects.get_or_create(username=username)
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
