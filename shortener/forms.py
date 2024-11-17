# shortener/forms.py
from django import forms

class URLForm(forms.Form):
    original_url = forms.URLField(widget=forms.TextInput(attrs={'placeholder': 'Enter URL'}), required=True)
