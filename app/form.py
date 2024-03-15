from django import forms
from .models import Imges

class ImageForm(forms.ModelForm):
    class Meta:
        model = Imges
        fields = '__all__'
        labels = {'photo':''}