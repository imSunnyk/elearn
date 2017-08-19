from __future__ import unicode_literals

from django.db import models
from courses.models import Course
from login.models import Person
from series.models import Series

import uuid


class Forum( models.Model ):
	from groups.models import Group

	name = models.CharField( max_length = 50 )
	group = models.ForeignKey( Group, related_name = 'group' )
	slug = models.CharField( max_length = 36)
	series = models.ForeignKey( Series )

	# override the save function
	def save( self, *args, **kwargs ):

		if not self.id:

			# Newly created object, so set slug
			self.slug = str( uuid.uuid4() ).replace( "-" , "") 

			super( Forum, self ).save( *args, **kwargs )


class Thread( models.Model ):

	name = models.CharField( max_length = 50 )
	author = models.ForeignKey( Person )
	desc = models.TextField()
	forum = models.ForeignKey( Forum, default = 111, editable=False )
	adate = models.DateField( auto_now = True )
	slug = models.CharField( max_length = 36)
	

	# override the save function
	def save( self, *args, **kwargs ):

		if not self.id:

			# Newly created object, so set slug
			self.slug = str( uuid.uuid4() ).replace( "-" , "") 

			super( Thread, self ).save( *args, **kwargs )


class Reply( models.Model ):

	desc = models.TextField()
	adate = models.DateField( auto_now = True )
	replied_to = models.ForeignKey( Thread )
	author = models.ForeignKey( Person )
