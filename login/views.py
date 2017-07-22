from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# import forms
from .forms import LoginForm

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
		if form.is_valid(): 

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


def change_pass( request ) : 

	return render( request, "login/recover.html" )