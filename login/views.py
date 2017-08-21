from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django import forms
from django.contrib.auth.models import User
from .models import Person

# import forms
from .forms import LoginForm

import uuid

@login_required
def logout_user( request ) :

	logout( request )
	return redirect( "/" )


def login_page( request ):

	# define the website context
	context = {

		"login_form" : LoginForm,
		"login_error" : 0,
		"err_message" : "",
		"debug" : ""

	}

	form = LoginForm( request.POST )

	if request.method == "POST" : 

		# check form validicity
		if form.is_valid() : 

			# login the user
			user = authenticate( username = form.cleaned_data[ "username" ], 
													 password = form.cleaned_data[ "password" ])

			#if the account is real
			if user is not None and user.is_active: 

				login( request, user )
				return redirect( "/my_courses" )

			else : 

				context[ "login_error" ] = 1
				context[ "err_message" ] = "Wrong username or password"				

		else :

			context[ "login_error" ] = 1
			context[ "err_message" ] = "Invalid form"

	return render( request, "login/login.html", context )


def change_pass( request, hash_code ):

	# declare the form
	class ChangePassForm(forms.Form):

		password = forms.CharField( widget = forms.PasswordInput )
		password_confirm = forms.CharField( widget = forms.PasswordInput )

	# define the varialbe that holds the form
	MyChangePassForm = ChangePassForm()

	# define context

	context = {

		"recover_pass_form" : MyChangePassForm,
		"user" : {},
		"debug" : "",
		"error" : ""

	}


	# then the form has been submitted

	if request.method == 'POST' : # change password button has been pressed

		# if the 2 passwords match

		form = ChangePassForm( request.POST )

		if form.is_valid() :

			password = request.POST[ "password" ]
			password_to_confirm = request.POST[ "password_confirm" ]

			if password == password_to_confirm :

				# update the user informations, then redirect the user to the main page

				user = User.objects.get( id = request.session[ "user" ][ "user_id" ] )
				user.set_password( password )
				user.save()

				person = Person.objects.filter( user_id = user.id ).update( hash_code = "" )

				return redirect( "/" )

			pass

		return render( request, "login/recover.html", context ) 

	else : 

		# this is the default page for the user

		# check if the key is valid

		try :

			user_data = Person.objects.values( 
				
					"user_id",
				
				).get( 
				
					hash_code = hash_code

				)

			if user_data[ "user_id" ] > 0 :

				request.session[ "user" ] = user_data

				# if yes, show recover page

				return render( request, "login/recover.html", context ) 

		except :

			# if not, show login 

			return redirect( "/" )


def send_email( request ) : 

	class MyEmailForm( forms.Form ) :

		email = forms.EmailField()


	my_email_form = MyEmailForm()

	context = {

		"debug" : {},
		"email_form" : my_email_form

	}

	if request.method == "POST" : 


		form = MyEmailForm( request.POST )

		if form.is_valid() : 

			try : 

				destination = form.cleaned_data[ "email" ]
				
				# create code
				code = str( uuid.uuid4() ).replace( "-" , "")
				
				# find user
				user = User.objects.get( email = form.cleaned_data[ "email" ] )

				# find user extension and set hashcode
				person = Person.objects.get( user_id = user.id )
				person.hash_code = code
				person.save()

				message = """ 
					Good day sir or madam. <br><br>
					The link for the recovery of your password is : 
					<a href = 'localhost:8000/login/change_pass/""" + str(  ) + """' > Click here </a> <br><br>
					If you encounter any problems, do not hesitate to contact us . <br><br>
					Best wishes and a happy day ! <br><br>
					Sincerely, <br><br>
					the AlpEduPro Team

				"""
		
				# try to send an email
				try : 

					mail = EmailMessage(
					    
						'AlpEduPro password recovery',
						"",
						'office@alpedupro.ro',
						[ destination_email ],
					
					)

					mail.content_subtype = "html"
					mail.body = message

				except :

					context[ "error" ] = 1
					context[ "message" ] = "Mail has not been sent, please contact your company admin"

			except : 

				pass

	return render( request, "login/send_email.html", context )