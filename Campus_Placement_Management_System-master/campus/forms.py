from django import forms

class DocumentForm(forms.Form):
    certi = forms.FileField(
        label="upload files"
    )