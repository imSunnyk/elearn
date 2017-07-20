from __future__ import unicode_literals

from django.db import models
from courses.models import Course
from groups.models import Group
from login.models import Person


class Forum( models.Model ):

	name = models.CharField( max_length = 50 )
	group = models.ForeignKey( Group, related_name = 'group' )


class Thread( models.Model ):

	name = models.CharField( max_length = 50 )
	author = models.ForeignKey( Person )
	desc = models.TextField()
	adate = models.DateField( auto_now = True )


class Reply( models.Model ):

	name = models.CharField( max_length = 50 )
	desc = models.TextField()
	adate = models.DateField( auto_now = True )
	replied_to = models.ForeignKey( Forum )
