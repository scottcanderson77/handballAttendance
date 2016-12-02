from django import forms
from django.contrib.auth.models import User, Group
from .models import report
from .models import folder

class ReportForm(forms.ModelForm):
    title = forms.CharField()
    timestamp = forms.DateTimeField()
    short_description = forms.CharField(max_length=30)
    detailed_description = forms.CharField(max_length=200)
    status_state = forms.CharField(max_length=10)
    location = forms.CharField(max_length=30)
    is_encrypted = forms.CharField(max_length=30)
    class Meta:
        model = report
        fields = ('short_description', 'document',)

class FolderForm(forms.Form):
    title = forms.CharField()

    def clean(self):
        try:
            folder.objects.get(title=self.cleaned_data['title'])
            # if we get this far, we have an exact match for this form's data
            raise forms.ValidationError("Exists already!")
        except folder.DoesNotExist:
            # because we didn't get a match
            pass
        return self.cleaned_data

