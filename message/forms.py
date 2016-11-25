from django import forms
from .models import *
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate


class MessageForm(forms.Form):
    title = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=50)),
            label=_("Title"), error_messages={
            'invalid': _("This value must contain only letters, numbers and underscores.")})

    body = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=500)), label=_("Body of Message"))

    sendToUser = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=50)),
            label=_("To User"), error_messages={
            'invalid': _("This user name doesn't exist")})

    #pub_date = forms.DateTimeField(
     #   widget=forms.DateTimeField())

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['sendToUser'])
        except User.DoesNotExist:
            raise forms.ValidationError(_("The username already exists. Please try another one."))
        return self.cleaned_data['sendToUser']

    def clean(self):
        return self.cleaned_data
