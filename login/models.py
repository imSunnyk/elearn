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