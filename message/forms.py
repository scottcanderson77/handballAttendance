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

    encrypt = forms.BooleanField(widget=forms.CheckboxInput(), required=False)

    #encrpyt = forms.boolean_check()
    #pub_date = forms.DateTimeField(widget=forms.DateTimeField())

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['sendToUser'])
            return self.cleaned_data['sendToUser']
        except User.DoesNotExist:
            raise forms.ValidationError(_("That username does not exist"))
        return self.cleaned_data['sendToUser']



class searchTitleForm(forms.Form):
    title = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=50)),
            label=_("Title"), error_messages={
            'invalid': _("This value must contain only letters, numbers and underscores.")})
    def clean(self):
        return self.cleaned_data


class searchSenderForm(forms.Form):
    sender = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=50)),
            label=_("Sender"), error_messages={
            'invalid': _("Invalid User")})
    def clean(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['sender'])
        except User.DoesNotExist:
            return self.cleaned_data['sender']
        raise forms.ValidationError(_("This is not a User"))

class decryptForm(forms.Form):
    privateKey = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=100000)), label=_("PrivateKey"))

    def clean(self):
        return self.cleaned_data


class DeleteForm(forms.Form):
    delete = forms.BooleanField(widget=forms.CheckboxInput(), required=False)

    def clean(self):
        return self.cleaned_data
