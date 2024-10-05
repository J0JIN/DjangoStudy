from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(min_length=3)
    password = forms.CharField(min_length=4)

class SignupForm(forms.Form):
    username = forms.CharField(min_length=3)
    password1 = forms.CharField(min_length=4, widget=forms.PasswordInput)
    password2 = forms.CharField(min_length=4, widget=forms.PasswordInput)
