from __future__ import unicode_literals

import os
import uuid

from django.contrib.auth.models import User
from django.db import models

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

	user = models.ForeignKey( 
		User, 
		related_name = "user" 
	)
	person_profile_pic = models.FileField( 
		upload_to = profile_pic, 
		blank = True 
	)
	person_type = models.CharField(
		max_length = 2,
		choices = TYPE_CHOICES,
		default = STUDENT,
	)
	person_active_courses = models.ManyToManyField( 
		Course 
	)
	person_hash_code = models.CharField( max_length = 36, default = "" )
	person_birthdate = models.DateField()
	person_series = models.ForeignKey( 
		"series.Series", 
		related_name = "person_user_series" 
	)

	# how the users are displayed
	def __unicode__( self ):

		return " %s " % ( self.user )

	# override the save function
	def save( self, *args, **kwargs ):
		
		# if a new user is created, and it is a tutor, create a new tutor object
		if not self.id and self.person_type == "TU" :

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

		return self.objects.values_list( 
			"person_active_courses" 
		).filter( id = stundent_id)


	class Meta :

		verbose_name = "User"

class Tutor( models.Model ) :

	person = models.ForeignKey( Person )

	def __unicode__( self ):

		return " %s " % ( self.person )