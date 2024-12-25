from django import forms
from . import models

class AddCloth(forms.ModelForm):
    class Meta:
        model = models.Cloth
        fields = ['title', 'description', 'image', 'slug']