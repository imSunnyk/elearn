from __future__ import unicode_literals

import os

from django.db import models
from django.contrib.auth.models import User


# define the path to the profile picture of a user
def profile_pic( self, file ):

	filename, file_extension = os.path.splitext( file )
	return "users/{0}{1}".format( self.user_id, file_extension )


class Person( models.Model ):

	# define the choices for the user_type

	TUTOR = "TU"
	STUDENT = "ST"

	TYPE_CHOICES = (

		( TUTOR, "Tutor" ),
		( STUDENT, "Student" ),

	)

	user_id = models.ForeignKey( User )
	profile_pic = models.FileField( upload_to = profile_pic )
	user_type = models.CharField(
		max_length = 2,
		choices = TYPE_CHOICES,
		default = STUDENT,
	)

	# how the users are displayed
	def __unicode__( self ):

		return " %s " % ( self.user_id )

	# override the save function
	def save( self, *args, **kwargs ):
		
		# if a new user is created, and it is a tutor, create a new tutor object
		if not self.id and self.user_type == "TU" :

			super( Person, self ).save( *args, **kwargs )
			tutor = Tutor( person = self )
			tutor.save()

		else :

			super( Person , self ).save( *args, **kwargs )

	class Meta :

		verbose_name = "User"

class Tutor( models.Model ) :

	person = models.ForeignKey( Person )

	def __unicode__( self ):

		return " %s " % ( self.person )