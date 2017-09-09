import uuid

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django import forms

from .models import Person

from .forms import LoginForm, ChangePassForm, MyEmailForm


@login_required
def logout_user( request ) :

	logout( request )
	return redirect( "/" )


def login_page( request ):

	my_login_form = LoginForm

	# define the website context
	context = {

		"login_form" : my_login_form,
		"login_error" : 0,
		"err_message" : "",
		"debug" : ""

	}

	my_form = LoginForm( request.POST )

	if request.method == "POST" : 

		# check form validicity
		if my_form.is_valid() : 

			# login the user
			my_user = authenticate( 
				username = my_form.cleaned_data[ "username" ], 
				password = my_form.cleaned_data[ "password" ]
			)

			#if the account is real
			if my_user is not None and my_user.is_active: 

				login( request, my_user )
				return redirect( "/my_courses" )

			else : 

				context[ "login_error" ] = 1
				context[ "err_message" ] = "Wrong username or password"				

		else :

			context[ "login_error" ] = 1
			context[ "err_message" ] = "Invalid form"

	return render( request, "login/login.html", context )


def change_pass( request, hash_code ):

	my_change_pass_form = ChangePassForm()
	
	context = {

		"recover_pass_form" : my_change_pass_form,
		"user" : {},
		"debug" : "",
		"error" : ""

	}


	# then the form has been submitted

	if request.method == 'POST' : # change password button has been pressed

		# if the 2 passwords match

		my_form = ChangePassForm( request.POST )

		if my_form.is_valid() :

			my_password = request.POST[ "password" ]
			my_password_to_confirm = request.POST[ "password_confirm" ]

			if my_password == my_password_to_confirm :

				# update the user informations, then redirect the user to the main page

				my_user = User.objects.get( 
					id = request.session[ "user" ][ "user_id" ]
				)
				my_user.set_password( password )
				my_user.save()

				my_person = Person.objects.filter( 
					user_id = user.id 
				).update( 
					person_hash_code = "" 
				)

				return redirect( "/" )

			pass

		return render( request, "login/recover.html", context ) 

	else : 

		# this is the default page for the user

		# check if the key is valid

		try :

			my_user_data = Person.objects.values( 
				
					"user_id",
				
				).get( 
				
					person_hash_code = hash_code

				)

			if my_user_data[ "user_id" ] > 0 :

				request.session[ "user" ] = my_user_data

				# if yes, show recover page

				return render( request, "login/recover.html", context ) 

		except :

			# if not, show login 

			return redirect( "/" )


def send_email( request ) : 

	my_email_form = MyEmailForm()

	context = {

		"debug" : {},
		"email_form" : my_email_form

	}

	if request.method == "POST" : 

		my_form = MyEmailForm( request.POST )

		if my_form.is_valid() : 

			try : 

				my_destination = my_form.cleaned_data[ "email" ]
				
				# create code
				my_code = str( uuid.uuid4() ).replace( "-" , "")
				
				# find user
				my_user = User.objects.get( 
					email = form.cleaned_data[ "email" ]
				)

				# find user extension and set hashcode
				my_person = Person.objects.get( user_id = user.id )
				my_person.person_hash_code = my_code
				my_person.save()

				message = """ 
					Good day sir or madam. <br><br>
					The link for the recovery of your password is : 
					<a href = 'localhost:8000/login/change_pass/""" + str( my_code ) + """' > Click here </a> <br><br>
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