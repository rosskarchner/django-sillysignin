from class_based_auth_views.views import LoginView, LogoutView

from .forms import SillyLoginForm


class SillyLogin(LoginView):
    """
    This CBV mostly exists to provide a login page with the
    silly form.
    """
    template_name = "registration/login.html"
    form_class = SillyLoginForm

    def get_success_url(self):
        return self.request.GET.get('next', '/')


class SillyLogout(LogoutView):
    """
    Just for API consistency...
    """
    pass
