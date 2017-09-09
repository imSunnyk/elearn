from __future__ import unicode_literals

import os
import uuid

from django.db import models

from courses.models import Course
from series.models import Series
from login.models import Person



def upload_file( self, file ):

	filename, file_extension = os.path.splitext( file )

	if( self.file_reply is None ) :

		return "forum/threads/{0}/{1}{2}".format( 
			self.file_thread.thread_slug, filename, file_extension 
		)

	else : 

		return "forum/threads/{0}/comms/{1}/{2}{3}".format( 
			self.file_thread.thread_slug, self.file_reply.reply_slug, filename, file_extension 
		)


class Forum( models.Model ):
	from groups.models import Group

	forum_name = models.CharField( max_length = 50 )
	forum_group = models.ForeignKey( 
		Group, 
		related_name = 'group', 
		on_delete = models.CASCADE 
	)
	forum_slug = models.CharField( max_length = 36)
	forum_series = models.ForeignKey( Series )

	# override the save function
	def save( self, *args, **kwargs ):

		if not self.id:

			# Newly created object, so set slug
			self.forum_slug = str( uuid.uuid4() ).replace( "-" , "") 

			super( Forum, self ).save( *args, **kwargs )


class Thread( models.Model ):

	thread_name = models.CharField( max_length = 50 )
	thread_author = models.ForeignKey( Person )
	thread_desc = models.TextField()
	thread_forum = models.ForeignKey( Forum, default = 111, editable=False )
	thread_adate = models.DateField( auto_now = True )
	thread_slug = models.CharField( max_length = 36)

	# override the save function
	def save( self, *args, **kwargs ):

		if not self.id:

			# Newly created object, so set slug
			self.thread_slug = str( uuid.uuid4() ).replace( "-" , "") 

			super( Thread, self ).save( *args, **kwargs )


class Reply( models.Model ):

	reply_slug = models.CharField( max_length = 36 )
	reply_desc = models.TextField()
	reply_adate = models.DateField( auto_now = True )
	reply_replied_to = models.ForeignKey( Thread )
	reply_author = models.ForeignKey( Person )

	# override the save function
	def save( self, *args, **kwargs ):

		if not self.id:

			# Newly created object, so set slug
			self.reply_slug = str( uuid.uuid4() ).replace( "-" , "") 

			super( Reply, self ).save( *args, **kwargs )


class FileUploaded( models.Model ):

	file_thread = models.ForeignKey( 
		Thread, 
		on_delete = models.CASCADE, 
		related_name = "thread" 
	)
	file_reply = models.ForeignKey( 
		Reply, 
		blank = True, 
		null = True, 
		on_delete = models.CASCADE, 
		related_name = "reply" 
	)	
	file_file_path = models.FileField( 
		upload_to = upload_file, 
		blank=True, 
		null=True 
	)
	file_slug = models.CharField( max_length = 36 )

	# override the save function
	def save( self, *args, **kwargs ):

		if not self.id:

			# Newly created object, so set slug
			self.file_slug = str( uuid.uuid4() ).replace( "-" , "") 

			super( FileUploaded, self ).save( *args, **kwargs )