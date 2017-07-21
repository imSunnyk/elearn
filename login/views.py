from django.shortcuts import render


def login( request ):

	return render( request, "login/login.html" )


def change_pass( request ) : 

	return render( request, "login/recover.html" )