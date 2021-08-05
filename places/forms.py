from django import forms
from django.forms import fields
from .models import Place

class PlaceForm(forms.ModelForm):

    class Meta:
        model = Place
        fields = ['name', 'location', 'description']
