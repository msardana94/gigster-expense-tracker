from django import forms
from django.contrib.auth.models import User
from django.forms.extras.widgets import SelectDateWidget
from django.conf import settings
from django.utils.encoding import (
    force_str
)
from django.utils.safestring import mark_safe
import datetime

class RegisterForm(forms.ModelForm):
    password_regex = r'[A-Za-z0-9]{8,}'
    first_name = forms.CharField(label="First Name", max_length=244)
    last_name = forms.CharField(label="Last Name", max_length=244)
    email = forms.EmailField(label="Email")
    password1 = forms.RegexField(regex=password_regex, widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label="Password", error_messages={'invalid': 'Minimum 8 characters'})
    password2 = forms.RegexField(regex=password_regex, widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label="Password (again)", error_messages={'invalid': 'Minimum 8 characters'})

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        count_pwd = 0
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                if type(field.widget) in (forms.TextInput, forms.DateInput):
                    field.widget = forms.TextInput(attrs={'placeholder': field.label, 'class': 'form-control', 'required': True})
                elif type(field.widget) in (forms.EmailInput,):
                    field.widget = forms.EmailInput(attrs={'placeholder': field.label, 'class': 'form-control', 'required': True})
                elif type(field.widget) in (forms.PasswordInput,):
                    count_pwd += 1
                    if count_pwd > 1:
                        field.widget = forms.PasswordInput(attrs={'placeholder': field.label, 'class': 'form-control', 'data-match': '#id_password1', 'required': True, 'pattern': self.password_regex, 'data-pattern-error': 'Minimum 8 characters'})
                    else:
                        field.widget = forms.PasswordInput(attrs={'placeholder': field.label, 'class': 'form-control', 'required': True, 'data-match': '#id_password1'})

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("The two password fields did not match.")
        return self.cleaned_data

    def clean_email(self):
        email = self.cleaned_data['email']
        if len(User.objects.filter(email=email)) > 0:
            raise forms.ValidationError(u'This account is already in use.')
        return email

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1','password2']


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email address")
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                "placeholder": self.fields[field].label,
                "class": "form-control",
                'required': True
            })

