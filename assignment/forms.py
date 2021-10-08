from django import forms
from .models import Post
from .models import ClassRoom
class PostCreateForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'id':'postdescription'}),required=False)
    #classroom = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control'}),queryset=ClassRoom.objects.all())
    class Meta:
        model = Post
        fields = ['description','file']