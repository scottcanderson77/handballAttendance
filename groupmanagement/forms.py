from django import forms
from django.contrib.auth.models import User, Group


class GroupingForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name',)

    def clean(self):
        return self.cleaned_data