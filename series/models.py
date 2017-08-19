from __future__ import unicode_literals

from django.db import models

class Series( models.Model ):

	name = models.CharField( max_length = 3, unique = True )

	class Meta:

	    verbose_name_plural = 'series'


 	# default display message
	def __unicode__( self ):

		return " %s Series " % ( self.name )