from __future__ import unicode_literals

from django.db import models
from courses.models import Course
from login.models import Person


class Group( models.Model ):

	name = models.CharField( max_length = 50 )
	slug = models.SlugField()
	location = models.CharField( max_length = 50 )
	course = models.ForeignKey( Course, related_name = 'course' )
	tutors = models.ManyToManyField( Person, related_name = 'tutors' )
	users = models.ManyToManyField( Person, related_name = 'users' )
