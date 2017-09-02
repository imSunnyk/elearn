from .models import Group
from django import forms

class GroupFormAdmin(forms.ModelForm):
	
	group_form_identifier = forms.CharField( widget = forms.HiddenInput(), label = "", initial = "default" )

	class Meta:
		model = Group
		fields = ( 'location', 'course', 'tutors', 'users', 'series', 'group_form_identifier'  )

	def save(self, commit=True):

		group = super(GroupFormAdmin, self).save(commit=False)

		if commit:
			group.save()

		return group