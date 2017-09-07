from __future__ import unicode_literals

import uuid
import os

from django.db import models
from login.models import Person

def upload_file( self, file ):

	filename, file_extension = os.path.splitext( file )

	if( self.reply is None ) :

		return "series/{0}/threads/{1}/{2}{3}".format( self.thread.series.name, self.thread.slug, filename, file_extension )

	else : 

		return "series/{0}/threads/{1}/comms/{2}/{3}{4}".format( self.thread.series.name, self.thread.slug, self.reply.slug, filename, file_extension )

#		return "series/{0}/threads/{1}/comms/{2}/{3}{4}".format( self.thread.series.name, self.thread.slug, self.reply.slug, filename, file_extension )


class Series( models.Model ):

	name = models.CharField( max_length = 3, unique = True )
	slug = models.CharField( max_length = 36 )

	class Meta:

	    verbose_name_plural = 'series'


 	# default display message
	def __unicode__( self ):

		return " %s Series " % ( self.name )

	# override the save function
	def save( self, *args, **kwargs ):

		if not self.id:

			# Newly created object, so set slug
			self.slug = str( uuid.uuid4() ).replace( "-" , "") 

			super( Series, self ).save( *args, **kwargs )	


class SeriesThread( models.Model ):

	name = models.CharField( max_length = 50 )
	author = models.ForeignKey( Person )
	desc = models.TextField()
	series = models.ForeignKey( Series, editable=False )
	adate = models.DateField( auto_now = True )
	slug = models.CharField( max_length = 36)

	# override the save function
	def save( self, *args, **kwargs ):

		if not self.id:

			# Newly created object, so set slug
			self.slug = str( uuid.uuid4() ).replace( "-" , "") 

			super( SeriesThread, self ).save( *args, **kwargs )


class SeriesReply( models.Model ):

	slug = models.CharField( max_length = 36 )
	desc = models.TextField()
	adate = models.DateField( auto_now = True )
	replied_to = models.ForeignKey( SeriesThread )
	author = models.ForeignKey( Person )

	# override the save function
	def save( self, *args, **kwargs ):

		if not self.id:

			# Newly created object, so set slug
			self.slug = str( uuid.uuid4() ).replace( "-" , "") 

			super( SeriesReply, self ).save( *args, **kwargs )


class SeriesFileUploaded( models.Model ):

	thread = models.ForeignKey( SeriesThread, on_delete = models.CASCADE, related_name = "thread" )
	reply = models.ForeignKey( SeriesReply, blank = True, null = True, on_delete = models.CASCADE, related_name = "reply" )	
	file = models.FileField( upload_to = upload_file, blank=True, null=True )
	slug = models.CharField( max_length = 36 )

	# override the save function
	def save( self, *args, **kwargs ):

		if not self.id:

			# Newly created object, so set slug
			self.slug = str( uuid.uuid4() ).replace( "-" , "") 

			super( SeriesFileUploaded, self ).save( *args, **kwargs )