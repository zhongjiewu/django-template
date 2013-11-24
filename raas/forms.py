from django import forms


class UploadDataFileForm(forms.Form):
    datafile = forms.FileField()
    domain = forms.CharField(max_length=50)
