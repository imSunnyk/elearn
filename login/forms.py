from django import forms

class LoginForm( forms.Form ):
	username = forms.CharField()
	password = forms.CharField( widget = forms.PasswordInput )

class ChangePassForm(forms.Form):

	password = forms.CharField( widget = forms.PasswordInput )
	password_confirm = forms.CharField( widget = forms.PasswordInput )

class MyEmailForm( forms.Form ) :

	email = forms.EmailField()