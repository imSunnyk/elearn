from .models import Page
from django import forms

class PageForm( forms.ModelForm ):
    
	page_desc = forms.CharField( widget = forms.Textarea, label = '' )

class CourseForm( forms.ModelForm ):
    
	course_desc = forms.CharField( widget = forms.Textarea, label = '' )	