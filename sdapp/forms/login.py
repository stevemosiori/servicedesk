from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label_suffix='')
    password = forms.CharField(widget=forms.PasswordInput)
    dob = forms.DateField()
