from django import forms
from django.contrib.auth.models import User, Group
from .models import report
from .models import folder
from .models import Document
from django.forms import ModelForm
class ReportForm(forms.Form):
    title = forms.CharField()
    short_description = forms.CharField(max_length=30)
    detailed_description = forms.CharField(max_length=200, widget=forms.Textarea(attrs={'rows':4, 'cols':40}))
    is_private = forms.BooleanField(required=False)
    # document = forms.FileField(label='Select a file',
    #                            required=False)
    # document = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label='Select a file', required=False)

    def clean(self):
        try:
            report.objects.get(title=self.cleaned_data['title'])
            # if we get this far, we have an exact match for this form's data
            raise forms.ValidationError("Exists already!")
        except report.DoesNotExist:
            # because we didn't get a match
            pass
        return self.cleaned_data
    # class Meta:
    #     model = report
    #     fields = ('title','detailed_description','short_description', 'document','is_private', 'location', 'is_encrypted', 'username_id' )
class FileForm(forms.Form):
    document = forms.FileField(label='Select a file', required=False)
    is_encrypted = forms.BooleanField(required=False, label="Encrypt File")
    document2 = forms.FileField(label='Select a file', required=False)
    is_encrypted2 = forms.BooleanField(required=False, label="Encrypt FIle")
    document3 = forms.FileField(label='Select a file', required=False)
    is_encrypted3 = forms.BooleanField(required=False, label="Encrypt File")



    class Meta:
        model = Document
        fields = {'document', 'is_encrypted','document1', 'is_encrypted1','document3', 'is_encrypted3'}

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

