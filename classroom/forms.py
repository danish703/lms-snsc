from django import forms
from .models import ClassRoom


class CreateClassRoom(forms.ModelForm):
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Python Django'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',}))
    class Meta:
        model = ClassRoom
        fields = ['subject','description','image']