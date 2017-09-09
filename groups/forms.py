from django import forms

from .models import Group


class GroupFormAdmin(forms.ModelForm):
	
	group_form_identifier = forms.CharField( 
		widget = forms.HiddenInput(), 
		label = "", 
		initial = "default" 
	)

	class Meta:
		model = Group
		fields = ( 
			'group_location', 
			'group_course', 
			'group_tutors', 
			'group_users', 
			'group_series', 
			'group_form_identifier'
		)

	def save( self, commit = True ):

		group = super( GroupFormAdmin, self ).save( commit = False )

		if commit:
			group.save()

		return group