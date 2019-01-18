from django import forms
from django.contrib.auth.models import User
from resume.models import UserProfileInfo
from django.core import validators


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    verify_email = forms.EmailField(label='Verify Email: ')
    text = forms.CharField(widget=forms.Textarea, required=True)
    botcatcher = forms.CharField(required=False,
                                    widget=forms.HiddenInput,
                                    validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError('verify email')


    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
