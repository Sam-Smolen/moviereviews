from django import forms
from .models import Movie, Review

class MovieForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'