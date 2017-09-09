from django import forms

class CommentForm( forms.Form ):

	desc = forms.CharField( widget = forms.Textarea )
	file = forms.FileField( 
		label = "Attach a file ", 
		widget = forms.ClearableFileInput( 
			attrs = { 'multiple' : True } ), 
		required = False 
	)

	
class AddTopicForm( forms.Form ):

	name = forms.CharField( max_length = 100 )
	desc = forms.CharField( widget = forms.Textarea )
	file = forms.FileField( 
		label = "Attach a file ", 
		widget = forms.ClearableFileInput( 
			attrs = { 'multiple' : True } ), 
		required = False
	)