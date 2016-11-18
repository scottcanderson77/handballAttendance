from django import forms
from django.contrib.auth.models import User, Group
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate



class MessageForm(forms.Form):
    title = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=50)),
            label=_("Title"), error_messages={
            'invalid': _("This value must contain only letters, numbers and underscores.")})

    body = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=500)), label=_("Body of Message"))

    pub_date = forms.DateTimeField(
        widget=forms.DateTimeField())

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The username already exists. Please try another one."))

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data