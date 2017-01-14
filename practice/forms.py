from django import forms
from django.contrib.auth.models import User, Group
from .models import practice
from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate


class PracticeForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=50)))

    short_description = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=50)))

    def clean(self):
        return self.cleaned_data
