from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from courses.models import Course
from login.models import Person, Tutor


class Group( models.Model ):

	name = models.CharField( max_length = 50 )
	slug = models.SlugField()
	location = models.CharField( max_length = 50 )
	course = models.ForeignKey( Course, related_name = 'course' )
	tutors = models.ManyToManyField( Tutor, related_name = 'tutors' )
	users = models.ManyToManyField( Person, related_name = 'users' )

	# override the save function
	def save( self, *args, **kwargs ):

		if not self.id:

			# Newly created object, so set slug
			self.slug = slugify( self.name )

		super( Group, self ).save( *args, **kwargs )
		

	def __unicode__( self ) : 

		return " %s " % ( self.name )

