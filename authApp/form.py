from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField, PasswordChangeForm,PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.forms.widgets import TextInput, NumberInput
from django.utils.translation import gettext_lazy,gettext as _
from django.forms import ModelForm
from .models import *
from django.contrib.auth import password_validation

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput)
    email = forms.CharField(required=True,widget=forms.EmailInput)

    class Meta:
        model=User
        fields = ['email','username','password1','password2']
        labels = {'email':"Email"}
        widgets = {'username':TextInput}
    
class Loginform(AuthenticationForm):

    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )

class Profile_Form(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('user',)
        widgets = {'locality':TextInput,'state':TextInput,'city':TextInput,'zipcode':NumberInput}
    
class PasswordChange(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Old password"),
        strip=False,
        widget = forms.PasswordInput(
            attrs={"autocomplete": "current-password", "autofocus": True}
        ),
    )
    new_password1 = forms.CharField(label=_("New Password"),strip=False,widget=forms.PasswordInput,help_text=password_validation.password_validators_help_text_html)
    new_password2 = forms.CharField(label=_('Confirm Password'),strip=False,widget=forms.PasswordInput)


class ForgetPassword(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )

class ResetPassword(SetPasswordForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
