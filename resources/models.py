from __future__ import unicode_literals

import os
import uuid

from django.template.defaultfilters import slugify
from django.db import models

from courses.models import Course


def file_path( self, file ):

	filename, file_extension = os.path.splitext( file )

	# define the folder containing the file
	if self.resource_doc_type == "AC" : 

		res_type = "activities"

	else :

		res_type = "resources"


	return "{0}/{1}/{2}{3}".format(
		self.resource_course.course_name, res_type, filename, file_extension
	)

class Resource( models.Model ):

	# define the choices for the user_type

	ACTIVITIES = "AC"
	COURSE = "CO"

	DOC_CHOICES = (

		( ACTIVITIES, "Activity" ),
		( COURSE, "Course" ),

	)

	resource_name = models.CharField( max_length = 50 )
	resource_course = models.ForeignKey( Course )
	resource_slug = models.CharField( max_length = 36)
	resource_document_path = models.FileField( upload_to = file_path )
	resource_doc_type = models.CharField( max_length = 2, choices = DOC_CHOICES )

 	# default display message
	def __unicode__( self ):

		return " %s : %s " % ( self.resource_course, self.resource_name )


	# override the save function
	def save( self, *args, **kwargs ):

		if not self.id:

			# Newly created object, so set slug
			self.resource_slug = str( uuid.uuid4() ).replace( "-" , "") 

			super( Resource, self ).save( *args, **kwargs )