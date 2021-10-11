from django import forms
from .models import Post
from .models import ClassRoom,Comment,Assignement
class PostCreateForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'id':'postdescription'}),required=False)
    #classroom = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control'}),queryset=ClassRoom.objects.all())
    class Meta:
        model = Post
        fields = ['description','file']


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'1','cols':'5'}), required=False)
    class Meta:
        model = Comment
        fields = ['comment',]


class AssignmentForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Aa'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Aa','id':'postdescription'}))
    deadline = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control','type':'date'}))
    marks = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model = Assignement
        exclude = ['classroom',]