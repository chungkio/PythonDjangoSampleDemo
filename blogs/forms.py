from django import forms
from django.contrib.auth.models import User
from tinymce.widgets import TinyMCE

from .models import Post


class PostForm(forms.ModelForm):
    body = forms.CharField(
        widget=TinyMCE(
            attrs={'required': False, 'cols': 30, 'rows': 100},
        )
    )

    class Meta:
        model = Post
        fields = '__all__'
