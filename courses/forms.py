from .models import Page
from django import forms

class PageForm( forms.ModelForm ):
    
	desc = forms.CharField( widget = forms.Textarea, label = '' )

class CourseForm( forms.ModelForm ):
    
	desc = forms.CharField( widget = forms.Textarea, label = '' )	