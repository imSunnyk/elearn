from __future__ import unicode_literals

import os

from django.db import models
from courses.models import Course


def file_path( self, file ):

	filename, file_extension = os.path.splittext( file )

	return "files/{0}/resources/{1}/{2}{3}".format(
		self.course, self.doc_type, filename, file_extension
	)

class File( models.Model ):

	# define the choices for the user_type

	ACTIVITIES = "AC"
	COURSE = "CO"

	DOC_CHOICES = (

		( ACTIVITIES, "Activity" ),
		( COURSE, "Course" ),

	)

	name = models.CharField( max_length = 50 )
	course = models.ForeignKey( Course )
	slug = models.SlugField()
	path = models.FileField( upload_to = file_path )
	doc_type = models.CharField( max_length = 2, choices = DOC_CHOICES ) 