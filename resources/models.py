from __future__ import unicode_literals

import os
import uuid

from django.db import models
from django.template.defaultfilters import slugify
from courses.models import Course


def file_path( self, file ):

	filename, file_extension = os.path.splitext( file )

	# define the folder containing the file
	if self.doc_type == "AC" : 

		res_type = "activities"

	else :

		res_type = "resources"


	return "{0}/{1}/{2}{3}".format(
		self.course.name, res_type, filename, file_extension
	)

class Resource( models.Model ):

	# define the choices for the user_type

	ACTIVITIES = "AC"
	COURSE = "CO"

	DOC_CHOICES = (

		( ACTIVITIES, "Activity" ),
		( COURSE, "Course" ),

	)

	name = models.CharField( max_length = 50 )
	course = models.ForeignKey( Course )
	slug = models.CharField( max_length = 36)
	document_path = models.FileField( upload_to = file_path )
	doc_type = models.CharField( max_length = 2, choices = DOC_CHOICES )

 	# default display message
	def __unicode__( self ):

		return " %s : %s " % ( self.course, self.name )


	# override the save function
	def save( self, *args, **kwargs ):

		if not self.id:

			# Newly created object, so set slug
			self.slug = str( uuid.uuid4() ).replace( "-" , "") 

			super( Resource, self ).save( *args, **kwargs )