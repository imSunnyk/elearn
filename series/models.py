from __future__ import unicode_literals

import uuid
import os

from django.db import models

from login.models import Person

def upload_file( self, file ):

	filename, file_extension = os.path.splitext( file )

	if( self.series_file_reply is None ) :

		return "series/{0}/threads/{1}/{2}{3}".format( 
			self.series_file_thread.series_thread_series.series_name, 
			self.series_file_thread.series_thread_slug, 
			filename, 
			file_extension 
		)

	else : 

		return "series/{0}/threads/{1}/comms/{2}/{3}{4}".format( 
			self.series_file_thread.series_thread_series.series_name, 
			self.series_file_thread.series_thread_slug, 
			self.series_file_reply.series_reply_slug, 
			filename, 
			file_extension 
		)


class Series( models.Model ):

	series_name = models.CharField( max_length = 3, unique = True )
	series_slug = models.CharField( max_length = 36 )

	class Meta:

	    verbose_name_plural = 'series'


 	# default display message
	def __unicode__( self ):

		return " %s Series " % ( self.series_name )

	# override the save function
	def save( self, *args, **kwargs ):

		if not self.id:

			# Newly created object, so set slug
			self.series_slug = str( uuid.uuid4() ).replace( "-" , "") 

			super( Series, self ).save( *args, **kwargs )	


class SeriesThread( models.Model ):

	series_thread_name = models.CharField( max_length = 50 )
	series_thread_author = models.ForeignKey( Person )
	series_thread_desc = models.TextField()
	series_thread_series = models.ForeignKey( Series, editable=False )
	series_thread_adate = models.DateField( auto_now = True )
	series_thread_slug = models.CharField( max_length = 36)

	# override the save function
	def save( self, *args, **kwargs ):

		if not self.id:

			# Newly created object, so set slug
			self.series_thread_slug = str( uuid.uuid4() ).replace( "-" , "") 

			super( SeriesThread, self ).save( *args, **kwargs )


class SeriesReply( models.Model ):

	series_reply_slug = models.CharField( max_length = 36 )
	series_reply_desc = models.TextField()
	series_reply_adate = models.DateField( auto_now = True )
	series_reply_replied_to = models.ForeignKey( SeriesThread )
	series_reply_author = models.ForeignKey( Person )

	# override the save function
	def save( self, *args, **kwargs ):

		if not self.id:

			# Newly created object, so set slug
			self.series_reply_slug = str( uuid.uuid4() ).replace( "-" , "") 

			super( SeriesReply, self ).save( *args, **kwargs )


class SeriesFileUploaded( models.Model ):

	series_file_thread = models.ForeignKey( 
		SeriesThread, 
		on_delete = models.CASCADE, 
		related_name = "series_file_thread"
	)
	series_file_reply = models.ForeignKey( 
		SeriesReply, 
		blank = True, 
		null = True, 
		on_delete = models.CASCADE, 
		related_name = "series_file_reply" 
	)	
	series_file_file = models.FileField( 
		upload_to = upload_file, 
		blank = True, 
		null = True 
	)
	series_file_slug = models.CharField( max_length = 36 )

	# override the save function
	def save( self, *args, **kwargs ):

		if not self.id:

			# Newly created object, so set slug
			self.series_file_slug = str( uuid.uuid4() ).replace( "-" , "") 

			super( SeriesFileUploaded, self ).save( *args, **kwargs )