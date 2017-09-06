from __future__ import unicode_literals

from django.db import models
from courses.models import Course
from login.models import Person
from series.models import Series

import os
import uuid

def upload_file( self, file ):

	filename, file_extension = os.path.splitext( file )

	if( type( self.reply ) is None ) :

		return "files/threads/{0}/{1}{2}".format( self.thread.slug, filename, file_extension )

	else : 

		return "files/threads/{0}/comms/{1}/{2}{3}".format( self.thread.slug, self.reply.slug, filename, file_extension )


class Forum( models.Model ):
	from groups.models import Group

	name = models.CharField( max_length = 50 )
	group = models.ForeignKey( Group, related_name = 'group', on_delete = models.CASCADE )
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

	slug = models.CharField( max_length = 36 )
	desc = models.TextField()
	adate = models.DateField( auto_now = True )
	replied_to = models.ForeignKey( Thread )
	author = models.ForeignKey( Person )

	# override the save function
	def save( self, *args, **kwargs ):

		if not self.id:

			# Newly created object, so set slug
			self.slug = str( uuid.uuid4() ).replace( "-" , "") 

			super( Reply, self ).save( *args, **kwargs )


class FileUploaded( models.Model ):

	thread = models.ForeignKey( Thread, on_delete = models.CASCADE, related_name = "thread" )
	reply = models.ForeignKey( Reply, blank = True, null = True, on_delete = models.CASCADE, related_name = "reply" )	
	file = models.FileField( upload_to = upload_file, blank=True, null=True )
	slug = models.CharField( max_length = 36 )

	# override the save function
	def save( self, *args, **kwargs ):

		if not self.id:

			# Newly created object, so set slug
			self.slug = str( uuid.uuid4() ).replace( "-" , "") 

			super( Reply, self ).save( *args, **kwargs )