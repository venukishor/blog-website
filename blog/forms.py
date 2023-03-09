from django import forms
from .models import Profile,BlogPost
from django.forms.widgets import ClearableFileInput

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'facebook', 'instagram', 'linkedin','image',)

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'slug', 'content', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title of the Blog'}),
            'slug': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Copy the title with no space and a hyphen in between'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Content of the Blog'}),
            'image':forms.ClearableFileInput(attrs={'multiple':True}),
        }