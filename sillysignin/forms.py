from django import forms
from django.contrib.auth import authenticate


class SillyLoginForm(forms.Form):
    username = forms.CharField(help_text="If this username doesn't exist,\
            a new account will be created.")

    def get_user(self):
        """
        Sends the form data right to authenticate.
        """
        user = authenticate(**self.cleaned_data)
        return user
