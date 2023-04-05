"""
Module with instances of the user interface
Returns:
    _type_: User object type
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.views.generic.edit import CreateView


class NewUserForm(UserCreationForm):
    """User creation form"""
    email = forms.EmailField(required=True)

    class Meta:
        """Fields and date for sending to POST methods"""
        model = User
        fields = UserCreationForm.Meta.fields + ("username", "email",
                                                 "password")

        def save(self, commit=True):
            """Saving user data to database

            Args:
                commit (bool, optional): Defaults to True.

            Returns:
                _type_: NewUserForm instance
            """
            user = super(NewUserForm, self).save(commit=False)
            user.email = self.cleaned_data["email"]
            if commit:
                user.save()
            return user
