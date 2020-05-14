from django import forms
from django.http import request
from .models import Blog, UserProfile
from django.contrib.auth.forms import UserCreationForm


class UserProfileForm(UserCreationForm):
    """
    create a form for blog model.
    """
    class Meta:
        model = UserProfile
        fields = ('name', 'email', 'gender', 'mobile', 'is_staff', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)


class AddUpdateBlogForm(forms.ModelForm):
    """
    create a form for blog model.
    """
    class Meta:
        model = Blog
        fields = ('name', 'email', 'title', 'body')

    def __init__(self, *args, **kwargs):
        super(AddUpdateBlogForm, self).__init__(*args, **kwargs)

