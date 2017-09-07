from __future__ import unicode_literals


import os
import uuid

from django.db import models
from django.contrib.auth.models import User
from courses.models import Course


# define the path to the profile picture of a user
def profile_pic( self, file ):

	filename, file_extension = os.path.splitext( file )
	return "users/{0}{1}".format( self.user_id, file_extension )


class Person( models.Model ):

	# define the choices for the user_type

	TUTOR = "TU"
	STUDENT = "ST"
	ADMIN = "AD"

	TYPE_CHOICES = (

		( TUTOR, "Tutor" ),
		( STUDENT, "Student" ),
		( ADMIN, "Admin" )

	)

	user = models.ForeignKey( User, related_name = "user" )
	profile_pic = models.FileField( upload_to = profile_pic, blank=True )
	user_type = models.CharField(
		max_length = 2,
		choices = TYPE_CHOICES,
		default = STUDENT,
	)
	active_courses = models.ManyToManyField( Course )
	hash_code = models.CharField( max_length = 36, default = "" )
	birthdate = models.DateField()
	series = models.ForeignKey( "series.Series", related_name = "user_series" )

	# how the users are displayed
	def __unicode__( self ):

		return " %s " % ( self.user )

	# override the save function
	def save( self, *args, **kwargs ):
		
		# if a new user is created, and it is a tutor, create a new tutor object
		if not self.id and self.user_type == "TU" :

			super( Person, self ).save( *args, **kwargs )
			tutor = Tutor( person = self )
			tutor.save()

		else :

			super( Person , self ).save( *args, **kwargs )

	# custom functions
	
	@classmethod
	def return_student_id( self, name_id ) : # function that return the student_id of a user

		return self.objects.all().get( user_id = name_id ).id

	@classmethod
	def return_student_courses( self, stundent_id ):

		return self.objects.values_list( "active_courses" ).filter( id = stundent_id)


	class Meta :

		verbose_name = "User"

class Tutor( models.Model ) :

	person = models.ForeignKey( Person )

	def __unicode__( self ):

		return " %s " % ( self.person )