from django import forms
from django.contrib.auth.models import User, Group
from .models import pracitce
from django.forms import ModelForm

class PracticeForm(forms.Form):
    title = forms.CharField()
    short_description = forms.CharField(max_length=30)
    is_active = forms.BooleanField(required=False)


    def clean(self):
        try:
            pracitce.objects.get(title=self.cleaned_data['title'])
            # if we get this far, we have an exact match for this form's data
            raise forms.ValidationError("Exists already!")
        except pracitce.DoesNotExist:
            # because we didn't get a match
            pass
        return self.cleaned_data
    # class Meta:
    #     model = report
    #     fields = ('title','detailed_description','short_description', 'document','is_private', 'location', 'is_