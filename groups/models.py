from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from courses.models import Course
from login.models import Person, Tutor
from series.models import Series


class Group( models.Model ):

	name = models.CharField( max_length = 100 )
	slug = models.SlugField()
	location = models.CharField( max_length = 50, blank = True)
	course = models.ForeignKey( Course, related_name = 'course', null = True, blank = True )
	tutors = models.ManyToManyField( Tutor, related_name = 'tutors', null = True, blank = True )
	users = models.ManyToManyField( Person, related_name = 'users', null = True, blank = True )
	series = models.ForeignKey( Series, related_name = 'series', null = True, blank = True )

	# override the save function
	def save( self, *args, **kwargs ):

		ok = 0

		if not self.id:

			# iterate group name

			possible_groups = Group.objects.all().filter( location = self.location, course = self.course, series = self.series )

			iterator = len( possible_groups )

			# forum creation

			from forum.models import Forum
			code = Course.objects.all().get( id = self.course.id ).code

			self.name = "Grupa " + str( iterator ) + "  " + str( code ) + " " + str( self.location ) + " " + str( self.series )

			# Newly created object, so set slug
			self.slug = slugify( self.name )

			forum_name = "Forum-" + str( self.name )
			
			try : 

				# try to find the last group, if not, means this is the first group created
				last_group_id = Group.objects.latest( "id" ).id
				
				forum = Forum( name = forum_name, group_id = last_group_id + 1, series_id = self.series.id )
				ok = 1

			except : 

				forum = Forum( name = forum_name, group_id = 1, series_id = self.series.id )
				ok = 1




				
			

		super( Group, self ).save( *args, **kwargs )
		
		if ok is 1 : 

			forum.save()

	def __unicode__( self ) : 

		return " %s " % ( self.name)

	@classmethod
	def return_student_group( self, stundent_id ):

		return self.objects.values( "name", "id", "course_id" ).filter( users = stundent_id )